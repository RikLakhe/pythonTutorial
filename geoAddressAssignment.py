import urllib.request, urllib.error, urllib.parse
import json

url = "http://py4e-data.dr-chuck.net/json?"

search_key = "University of Oxford"
api_key = 42

parms = dict()
parms['address'] = search_key
parms['key'] = api_key

url_with = url+urllib.parse.urlencode(parms)

data = urllib.request.urlopen(url_with)
res = data.read().decode()

try:
    js = json.loads(res)
except:
    js = None

if not js or len(js)<1 or 'status' not in js or js['status'] != 'OK':
    print('Loaction not found!')
else:
    place_id = js['results'][0]['place_id']
    print("here",place_id)