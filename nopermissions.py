#libraries for OAuth
import requests
from requests import OAuth1

#library to parse JSON
import json

#keys
client_key = '...enter your unique client key...'
client_secret = '...enter your unique client secret...'

#Using OAuth1 to make a simple query request on when your application doesn't require any permissions
query_url = 'http:'
queryoauth = OAuth1(client_key, client_secret, signature_type='query')
r = requests.get(url=query_url, auth=queryoauth)

print(r.content)

#then to parse the json result
result = json.loads(r.content.decode('utf8'))
print(result)
