from __future__ import division
import requests
import json
import sys
from Route import Route
from segmentInfo import SegmentInfo
from RouteInfo import RouteInfo


class RouteQuery:
    total_duration = 0
    total_duration_in_traffic = 0

    def __init__(self,Route, apikey):
        self.route1 = Route
        self.apikey = apikey

    def query(self): # returns a Route Info for the desired route. Broken up by leg

        routeInfo = RouteInfo()
        routeResponse = ''
        for index in range(len(self.route1.segments[:-1])):
            response = self.query_route(self.route1.segments[index].startPoint, self.route1.segments[index+1].startPoint)
            duration, duration_in_traffic = self.response_Parse(response)
            name = self.createName(self.route1.segments[index].name, self.route1.segments[index+1].name)
            routeResponse += self.segmentResponse(duration, duration_in_traffic, name)
            routeInfo.addSegment(SegmentInfo(name, duration, duration_in_traffic))

        response = self.query_route(self.route1.segments[-1].startPoint, self.route1.destination)
        duration, duration_in_traffic = self.response_Parse(response)
        name = self.createName(self.route1.segments[-1].name, self.route1.destination[1])
        routeResponse += self.segmentResponse(duration, duration_in_traffic, name)
        routeInfo.addSegment(SegmentInfo(name, duration, duration_in_traffic))
        routeResponse += self.segmentSummary()
        routeInfo.addResponse(routeResponse)

        return routeInfo

    def query_route(self, origin,destination): #queries google api for route results

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

    def segmentResponse(self,duration,duration_in_traffic, name): #builds string outlining current situation of segment

        valduration = duration['value']
        valduration_in_traffic = duration_in_traffic['value']
        self.total_duration += valduration
        self.total_duration_in_traffic += valduration_in_traffic
        slowdown = (valduration_in_traffic-valduration)//60
        percentSlowdown = valduration_in_traffic/valduration



        if (percentSlowdown > 0.9):
            segmentResponse = ("Segment %s is slower by %s minutes. " %((name), (slowdown)))

        else:
            segmentResponse = ''

        return segmentResponse

    def segmentSummary(self): #returns string summarizing total slowdown of route

        routeSlowdown = (self.total_duration_in_traffic-self.total_duration)//60

        segmentSummary = "Overall your route is slower by %s minutes. " %(routeSlowdown)

        return segmentSummary

