# this program uses urllib to make a request to a web page 
# receive data back, decode it and displays it

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in  fhand:
    print( line.decode().strip() )