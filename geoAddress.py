import urllib.parse, urllib.request, urllib.error
import json

locationIq_token = 'gg'
locationIq_url='https://us1.locationiq.com/v1/search.php?'

while True:
    input_address = input('Enter address = ')

    if len(input_address)<1: break

    url = locationIq_url+urllib.parse.urlencode({
        "key": locationIq_token,
        "q":input_address,
        "format":"json"
    })

    print('Data from,',url)

    uh = urllib.request.urlopen(url)
    data= uh.read().decode()
    print('Data got,',data, 'length',len(data))

    try:
        json_data = json.loads(data)
    except:
        json_data = None

    if not json_data or len(json_data) < 1:
        print('=====Failed to recieve Data=====')
        print('data')
        continue

    lat = json_data[0]['lat']
    lon = json_data[0]['lon']
    location_name = json_data[0]['display_name']

    print('=====data recieved =======')
    print('lat = ',lat)
    print('lon = ',lon)
    print('name = ',location_name)
