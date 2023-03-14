from app.netsuite import NetsuiteRequest

netsuite = NetsuiteRequest()

# Replace with your SuiteQL-compliant query below
query = "SELECT * FROM Customer"

# Returns JSON as presented here. You may wish to normalize in NetsuiteRequest.
data = netsuite.suiteql_query(query)