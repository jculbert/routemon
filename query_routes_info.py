#!/usr/bin/env python

import mysql.connector

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

query = 'select * from RouteInfo'

cursor.execute(query)

for (route_info_num, route_num, segment_info, summary, date_time) in cursor:
    print route_info_num
    print route_num
    print segment_info
    print summary
    print date_time


cursor.close()
cnx.close()