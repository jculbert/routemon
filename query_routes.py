#!/usr/bin/env python
import json
import mysql.connector

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

query = 'select * from Routes'

cursor.execute(query)

for (route_num, user_name, route_name, segments, destination) in cursor:
    print route_name
    print segments
    print destination
    segments_list = json.loads(segments)
    print segments_list

cursor.close()
cnx.close()