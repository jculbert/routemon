import requests
import json
import sys

api=sys.argv[1]

def main(api):

    url ='https://maps.googleapis.com/maps/api/directions/json'

    params = dict(
        origin = '43.865926, -79.289759',
        destination ='43.380903, -80.496452',
        key = api ,
        departure_time = 'now',
        avoid ='tolls'
    )

    r = requests.get(url=url,params=params)
    q= r.json()
    duration_in_traffic = (q['routes'][0]['legs'][0]['duration_in_traffic']['text'])
    duration_no_traffic =(q['routes'][0]['legs'][0]['duration']['text'])
    print 'Duration in Traffic is ',duration_in_traffic
    print 'Duration without Traffic is',duration_no_traffic

main(api)