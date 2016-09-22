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

    def __init__(self, apikey):
        self.apikey = apikey

    def query(self, route): # returns a Route Info for the desired route. Broken up by leg

        routeInfo = RouteInfo(route.route_num)
        summary = ''
        for index in range( len(route.points[:-1]) ):
            p1 = route.points[index]
            p2 = route.points[index+1]
            response = self.query_route(p1.location, p2.location)
            duration, duration_in_traffic = self.response_Parse(response)

            name = self.createName(p1.name, p2.name)
            summary += self.segmentSummary(duration, duration_in_traffic, name)
            routeInfo.add_segment( SegmentInfo(name, duration, duration_in_traffic) )

        summary += self.overallSummary()
        routeInfo.add_summary(summary)

        return routeInfo

    def query_route(self, origin, destination): #queries google api for route results

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

    def createName(self, origin, destination):
        link = ' to '
        name = origin + link + destination

        return name

    def segmentSummary(self, duration, duration_in_traffic, name): #builds string outlining current situation of segment

        valduration = duration['value']
        valduration_in_traffic = duration_in_traffic['value']
        self.total_duration += valduration
        self.total_duration_in_traffic += valduration_in_traffic
        slowdown = (valduration_in_traffic-valduration)//60
        percentSlowdown = valduration_in_traffic/valduration

        if (percentSlowdown > 0.9):
            summary = ("Segment %s is slower by %s minutes. " %((name), (slowdown)))

        else:
            summary = ''

        return summary

    def overallSummary(self): #returns string summarizing total slowdown of route

        routeSlowdown = (self.total_duration_in_traffic-self.total_duration)//60

        summary = "Overall your route is slower by %s minutes. " %(routeSlowdown)

        return summary

