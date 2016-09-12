import requests
import json
import sys
from Route import Route
from segmentInfo import SegmentInfo
from RouteInfo import RouteInfo

class RouteQuery:
    def __init__(self,Route, apikey):
        self.route1 = Route
        self.apikey = apikey

    def query(self):

        routeInfo = RouteInfo()
        for index in range(len(self.route1.segments[:-1])):
            response = self.query_route(self.route1.segments[index].startPoint, self.route1.segments[index+1].startPoint)
            duration, duration_in_traffic = self.response_Parse(response)
            routeInfo.addSegment(SegmentInfo(self.route1.segments[index].name, duration, duration_in_traffic))

        response = self.query_route(self.route1.segments[-1].startPoint, self.route1.destination)
        duration, duration_in_traffic = self.response_Parse(response)
        routeInfo.addSegment(SegmentInfo(self.route1.segments[-1].name, duration, duration_in_traffic))

        return routeInfo

    def query_route(self, origin,destination):

        url ='https://maps.googleapis.com/maps/api/directions/json'

        params = dict(
            origin = origin,
            destination = destination ,
            key = self.apikey ,
            departure_time = 'now',
            avoid ='tolls'
        )

        r = requests.get(url=url,params=params).json()
        return r

    def response_Parse(self, response):

        duration = response['routes'][0]['legs'][0]['duration']
        duration_in_traffic = response['routes'][0]['legs'][0]['duration_in_traffic']

        return (duration, duration_in_traffic)

    def createName(self,origin,destination):
        link = ' to '
        name = origin + link + destination

        return name
