#libraries for OAuth
import requests
from requests_oauthlib import OAuth1

#keys
client_key = '...enter your unique client key...'
client_secret = '...enter your unique client secret...'

#Using OAuth1 to make a simple query request on when your application doesn't require any permissions
query_url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20%3D%20%22YHOO%22%20and%20startDate%20%3D%20%222009-09-11%22%20and%20endDate%20%3D%20%222010-03-10%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
queryoauth = OAuth1(client_key, client_secret, signature_type='query')
r = requests.get(url=query_url, auth=queryoauth)

print(r.content)

#library to parse JSON
import json

result = json.loads(r.content.decode('utf8'))
print(result)
