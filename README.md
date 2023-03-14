# netsuite-basics

[Oracle NetSuite](https://netsuite.com) is one of the most popular cloud ERP 
systems. But on a recent client engagement, I was surprised by how relatively
little sample code and support resources seemed to be available for those 
wanting to automate NetSuite REST workflows using Python. This starter app aims
to demonstrate the basics needed to begin receiving responses via the API
without (crucially) any manual authentication steps.

## Requirements

* Python 3.11
* Dependencies specified in `requirements.txt`
* NetSuite account and sufficiently permissioned access token

## NetSuite Resources

NetSuite REST Web Services use SuiteQL, a query language based on SQL-92. It
supports querying records within NetSuite, with some guardrails designed to
help keep your data safe from SQL injection and other threats.

* [Using SuiteQL](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_156257799794.html)
* [Executing SuiteQL Queries Through REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_157909186990.html)