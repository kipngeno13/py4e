# this program accepts a link from the user, visits it, reads it and extracts anchor tags from it.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import  ssl

# this ignores ssl errors 

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



link = input("Input link : ")
link_handle = urllib.request.urlopen(link,context=ctx).read()
unsouped = BeautifulSoup(link_handle,'html.parser')

anchors = unsouped('a')

for anchor in anchors:
    print(anchor.get('href',None))

