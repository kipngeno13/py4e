# this program attempts to test if it can pulll data from twitter


import urllib.request, urllib.parse, urllib.error
import ssl

from twurl import augment


print("---connecting to twitter---")

url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
            {'screen-name':'eno_koech','count':'2'})
print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url,context=ctx)
data = connection.read()
print(data)

headers  = dict(connection.getheaders())
print(headers)