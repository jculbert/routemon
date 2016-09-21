#!/usr/bin/env python
import mysql.connector
import datetime
from datetime import timedelta

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

insert_stmt = (
  "INSERT INTO Routes (user_name, route_name, segments, destination, query_time) "
  "VALUES (%s, %s, %s, %s, %s)"
)

now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 1000)
data = ('robert', 'Home to Downtown Toronto', '[{"name": "Home", "location": "43.381355,-80.494107"},{"name": "427 at 401", "location": "43.665446, -79.572735"}]', '{"name": "Roy Thompson Hall", "location": "43.645825, -79.386790"}', now_plus_10)
cursor.execute(insert_stmt, data)

cnx.commit()

cursor.close()
cnx.close()