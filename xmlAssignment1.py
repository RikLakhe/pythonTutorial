import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET


#ignores ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_fetched = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_329408.xml', context=ctx).read()
tree_data = ET.fromstring(data_fetched)

nodes = tree_data.findall('.//count')

counter = 0

for item in nodes:
    counter += int(item.text)


print('count =',counter)



