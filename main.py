import requests
import json
import sys
from route import Route
#from routeLeg import RouteLeg
from routeResponse import RouteResponse

#apikey=sys.argv[1]

apikey = 'AIzaSyDuiSPpsDNUl79MvqjbQnd32MPQ2nYhfds'

def query_route(origin,destination):

    url ='https://maps.googleapis.com/maps/api/directions/json'

    params = dict(
        origin = origin,
        destination = destination ,
        key = apikey ,
        departure_time = 'now',
        avoid ='tolls'
    )

    r = requests.get(url=url,params=params).json()
    return r
    #q= r.json()
    #duration_in_traffic = (q['routes'][0]['legs'][0]['duration_in_traffic']['text'])
    #duration_no_traffic =(q['routes'][0]['legs'][0]['duration']['text'])
    #print 'Duration in Traffic is ',duration_in_traffic
    #print 'Duration without Traffic is',duration_no_traffic

waypoints = []
waypoints.append('43.267880, -79.892870')
waypoints.append('43.526907, -80.262387')
waypoints.append('43.474657, -80.546447')


route1 = Route('43.865926, -79.289759', '43.380903, -80.496452' , waypoints )
#query_route(route1)



if route1.waypoints == None:
    response=query_route(route1.origin, route1.destination)

    routeInfo = RouteResponse(response)

else:
    routeInfo = []
    response  = query_route(route1.origin, route1.waypoints[0])
    routeInfo.append(RouteResponse(response))

    if len(route1.waypoints) == 1:
        response = query_route(route1.waypoints[0], route1.destination)
        routeInfo.append(RouteResponse(response))

    else:
        for index in range(len(route1.waypoints[:-1])):
            response = query_route(route1.waypoints[index], route1.waypoints[index+1])
            routeInfo.append(RouteResponse(response))

        response = query_route(route1.waypoints[-1], route1.destination)
        routeInfo.append(RouteResponse(response))

hello = "false"










