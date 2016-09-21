#!/usr/bin/env python
import json
import mysql.connector
from segment import Segment
from Route import Route
from routeQuery import RouteQuery
import datetime

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()
cnx2 = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor2 = cnx2.cursor()


apikey ='AIzaSyDuiSPpsDNUl79MvqjbQnd32MPQ2nYhfds'

query = 'select * from Routes'
now = datetime.datetime.now()
cursor.execute(query)
#queries all routes in Routes table with a route info
for (route_num, user_name, route_name, segments, destination,query_time) in cursor:
    query_time_conv = datetime.datetime.strptime(query_time,"%Y-%m-%d %H:%M:%S.%f" )

    if query_time_conv > now :
        print "Valid Future Timestamp"
        segments_list = json.loads(segments)
        segments = []
        for segment in segments_list:
            segmentAdded = Segment(segment['location'],segment['name'])
            segments.append(segmentAdded)

        destination = json.loads(destination)


        destinationAdded = (destination['location'],destination['name'])
        route = Route(segments, destinationAdded)
        routeQuery = RouteQuery(route,apikey)
        routeInfo= routeQuery.query()
        routeInfoJ = (routeInfo.to_JSON())


        insert_stmt = (
            "INSERT INTO RouteInfo (route_info, route_num, route_info_response) VALUES (%s,%s,%s)")
        data = (routeInfoJ, route_num, routeInfo.response)
        print 'Route Queried'
        cursor2.execute(insert_stmt, data)
        cnx2.commit()
    else:
        print "Timestamp in Past"
        break

cursor.close()
cnx.close()
cursor2.close()
cnx2.close()




