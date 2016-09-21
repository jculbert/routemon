#!/usr/bin/env python
import mysql.connector
import datetime
from datetime import timedelta


cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()


now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 1000)

insert_stmt = (
  "INSERT INTO Routes (user_name, route_name, segments, destination, query_time) "
  "VALUES (%s, %s, %s, %s, %s)"
)

data = ('jeff', 'all_401', '[{"name": "Work", "location": "43.859122,-79.349120"},{"name": "401 to 407", "location": "43.773128, -79.339441"}, {"name": "407 to Home", "location": "43.588272,-79.810457"}]', '{"name": "Home", "location": "43.381355,-80.494107"}', now_plus_10)
cursor.execute(insert_stmt, data)

cnx.commit()

cursor.close()
cnx.close()

