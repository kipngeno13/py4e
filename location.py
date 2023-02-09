# this program should take an address, get data about it and display it.
# currently lacking api authentification from maps

import json
import urllib.request, urllib.parse, urllib.error

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location: ')
    if len(address)<1:
        break
    
    url = service_url + urllib.parse.urlencode(
        {'address':address}

    )
    print('retreiving',url)
    handle = urllib.request.urlopen(url)
    retrieved = handle.read().decode()

    print('retrieved ',len(retrieved),' characters')

    try:
        js = json.loads(retrieved)
    except:
        js = None

    if not js or 'status' not in js or js['status'] !='OK':
        print('--failed--')
        # print(retrieved)
        continue
    
    # print(json.dumps(js,indent=4))