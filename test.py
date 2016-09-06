#!/usr/bin/env python
import mysql.connector

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

insert_stmt = (
  "INSERT INTO Routes (user_name, route_name, origin, destination, waypoints) "
  "VALUES (%s, %s, %s, %s, %s)"
)
data = ('jeff', 'all_401', '123,456', '321,987', '["111,222", "333,444"]')
cursor.execute(insert_stmt, data)

cnx.commit()

cursor.close()
cnx.close()