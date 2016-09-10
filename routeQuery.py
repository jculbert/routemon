import requests
import json
import sys
from route import Route
from segmentInfo import SegmentInfo

class RouteQuery:
    def __init__(self,Route, apikey):
        self.route1 = Route
        self.apikey = apikey

    def query(self):


        if self.route1.waypoints == None:
            segmentInfo = []
            response = self.query_route(self.route1.origin, self.route1.destination)
            name = self.createName(self.route1.originText,self.route1.destinationText)
            duration, duration_in_traffic = self.response_Parse(response)
            segmentInfo = SegmentInfo(name,duration,duration_in_traffic)

        else:
            segmentInfo = []
            response = self.query_route(self.route1.origin, self.route1.waypoints[0][0])
            name = self.createName(self.route1.originText,self.route1.waypoints[0][1])
            duration, duration_in_traffic = self.response_Parse(response)
            segmentInfo.append(SegmentInfo(name,duration,duration_in_traffic))
            #segmentInfo.append(SegmentInfo(response))

            if len(self.route1.waypoints) == 1:
                response = self.query_route(self.route1.waypoints[0][0], self.route1.destination)
                name = self.createName(self.route1.waypoints[0][1],self.destinationText)
                duration, duration_in_traffic = self.response_Parse(response)
                segmentInfo.append(SegmentInfo(name, duration, duration_in_traffic))
                #segmentInfo.append(SegmentInfo(response))

            else:
                for index in range(len(self.route1.waypoints[:-1])):
                    response = self.query_route(self.route1.waypoints[index][0], self.route1.waypoints[index + 1][0])
                    name = self.createName(self.route1.waypoints[index][1], self.route1.waypoints[index +1][1])
                    duration, duration_in_traffic = self.response_Parse(response)
                    segmentInfo.append(SegmentInfo(name, duration, duration_in_traffic))

                    #segmentInfo.append(SegmentInfo(response))

                response = self.query_route(self.route1.waypoints[-1][0], self.route1.destination)
                name = self.createName(self.route1.waypoints[-1][1], self.route1.destinationText)
                duration, duration_in_traffic = self.response_Parse(response)
                segmentInfo.append(SegmentInfo(name, duration, duration_in_traffic))
                #segmentInfo.append(SegmentInfo(response))

        return segmentInfo

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
