#!/usr/bin/env python
import mysql.connector

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

insert_stmt = (
  "INSERT INTO Routes (user_name, route_name, segments, destination) "
  "VALUES (%s, %s, %s, %s)"
)
data = ('jeff', 'all_401', '[{"name": "Work To 401", "location": "43.859122,-79.349120"}, {"name": "401 to 407", "location": "43.588272,-79.810457"}]', '{"name": "Home", "location": "43.381355,-80.494107"}')
cursor.execute(insert_stmt, data)

cnx.commit()

cursor.close()
cnx.close()

