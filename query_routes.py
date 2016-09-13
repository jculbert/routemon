#!/usr/bin/env python
import json
import mysql.connector
from segment import Segment
from Route import Route
from routeQuery import RouteQuery

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

apikey = 'AIzaSyDuiSPpsDNUl79MvqjbQnd32MPQ2nYhfds'

query = 'select * from Routes'

cursor.execute(query)

#for (route_num, user_name, route_name, segments, destination) in cursor:
    #print route_name
    #print segments
    #print destination
    #segments_list = json.loads(segments)
    #print segments_list

for (route_num, user_name, route_name, segments, destination) in cursor:
    segments_list = json.loads(segments)
    segments = []
    for segment in segments_list:
        print segment['location']
        print segment['name']
        segmentAdded = Segment(segment['location'],segment['name'])
        segments.append(segmentAdded)

    destination = json.loads(destination)
    print destination['location']
    print destination['name']

    destinationAdded = (destination['location'],destination['name'])
    route = Route(segments, destinationAdded)
    routeQuery = RouteQuery(route,apikey)
    routeInfo = routeQuery.query()
    print (routeInfo.to_JSON())
    routeInfoJ = (routeInfo.to_JSON())

    insert_stmt = (
        "INSERT INTO RouteInfo (route_info, route_num) VALUES (%s,%s)")
    print type(routeInfoJ)
    print type(route_num)
    data = (routeInfoJ, route_num,)
    print data
    print type(data)
    cursor.execute(insert_stmt, data)
    cnx.commit()


cursor.close()
cnx.close()




