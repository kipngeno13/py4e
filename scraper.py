# this is a program that visits webpages, reads it and extracts anchor tags

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm").read()
souped = BeautifulSoup(fhand,'html.parser')

tags = souped('a')

for tag in tags:
    print(tag.get('href',None))
