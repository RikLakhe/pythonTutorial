import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_329409.json"

recieverd_data = urllib.request.urlopen(url)
data = recieverd_data.read().decode()

try:
    js = json.loads(data)
except:
    js = None

if not js or len(js)<1:
    print('=====Data not Recieved ==== Error ! ======')

# print(json.dumps(js,indent=4))
count = 0

for item in js["comments"]:
    # print('count=',item["count"])
    count+=int(item["count"])

print('Total:',count)