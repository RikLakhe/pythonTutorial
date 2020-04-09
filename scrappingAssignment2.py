import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignores ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#link position and loop
position = 18
loop = 7

# first link
url = "http://py4e-data.dr-chuck.net/known_by_Shauntel.html"

for x in range(0,loop):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href')
    print("loop position",tags[position-1])
