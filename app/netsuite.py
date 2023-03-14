import json
import requests
import os

from dotenv import load_dotenv
from oauthlib import oauth1
from requests_oauthlib import OAuth1Session

class NetsuiteRequest:

    def __init__(self):
        # See .env.example for required env variable structure
        load_dotenv()

        self.account = os.environ['NETSUITE_ACCOUNT']
        self.client = OAuth1Session(
            client_key = os.environ['NETSUITE_CONSUMER_KEY'],
            client_secret = os.environ['NETSUITE_CONSUMER_SECRET'],
            resource_owner_key = os.environ['NETSUITE_ACCESS_TOKEN'],
            resource_owner_secret = os.environ['NETSUITE_TOKEN_SECRET'],
            realm = self.account,
            signature_method = oauth1.SIGNATURE_HMAC_SHA256
        )

    def parse_response(self, response):
        response_json = json.loads(response.text)

        count = response_json['count']
        items = response_json['items']
        total = response_json['total']
        offset = response_json['offset']

        if response_json['hasMore']:
            next_link = next(link for link in response_json['links'] if link['rel'] == "next")['href']
        
        else: next_link = None

        return count, items, total, offset, next_link

    def suiteql_query(self, query):
        self.query = query

        url = f"https://{self.account}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql/"
        headers = {
            "Prefer": "transient",
            "Content-Type": "application/json"
        }

        body = json.dumps({"q": self.query})
        data = []

        while True:
            response = self.client.post(url=url, data=body, headers=headers)

            try: response.raise_for_status()

            except requests.exceptions.HTTPError as e:
                raise Exception(f"SuiteQL request failed. Error: {e}. Response Body: {response.text}")
            
            count, items, total, offset, next_link = self.parse_response(response)
            print(f"Received {offset + count} of {total} results.")

            data = data + items

            if next_link: url = next_link
            else: break

        # return pd.json_normalize(data) # Requires pandas
        return data
