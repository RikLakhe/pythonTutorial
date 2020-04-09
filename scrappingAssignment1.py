import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignores ssl certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('enter = ')
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_329406.html', context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span',{'class':"comments"})

count = 0

for tag in tags:
    count = float(tag.text) + count

print(count)