#!/usr/bin/env python
import mysql.connector
import json
import datetime
from datetime import timedelta

cnx = mysql.connector.connect(user='routemon', password='blart', database='RouteMon')
cursor = cnx.cursor()

# Clear the Routes table
cursor.execute("delete from Routes")

insert_stmt = (
  "INSERT INTO Routes (user_name, route_name, points, query_time) "
  "VALUES (%s, %s, %s, %s)"
)

# work_loc = "43.856988,-79.348338"
# home_loc = "43.381360,-80.494168"
# h401_h6_loc = "43.454654,-80.126614"
# h401_h407_loc = "43.571845,-79.830654"
# h401_h404_loc = "43.767985,-79.364130"
#
# name = 'To home all 401'
# segments = [
#     {"name": "Work To 401", "location": work_loc},
#     {"name": "401 to 407", "location": h401_h404_loc},
#     {"name": "407 to 6", "location": h401_h407_loc},
#     {"name": "6 to home", "location": h401_h6_loc}
# ]
# destination = {"name": "Home", "location": home_loc}

#data = ('jeff', name, json.dumps(segments), json.dumps(destination))

now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 1000)
data = ('robert', 'Home to Downtown Toronto', '[{"name": "Home", "location": "43.381355,-80.494107"},{"name": "427 at 401", "location": "43.665446, -79.572735"},{"name": "Roy Thompson Hall", "location": "43.645825,-79.386790"}]', now_plus_10)
cursor.execute(insert_stmt, data)

cnx.commit()

# name = 'To work all 401'
# segments = [
#     {"name": "Home to 6", "location": home_loc},
#     {"name": "6 to 407", "location": h401_h6_loc},
#     {"name": "407 to 404", "location": h401_h407_loc},
#     {"name": "404 to work", "location": h401_h404_loc}
# ]
# destination = {"name": "Work", "location": work_loc}
#
# data = ('jeff', name, json.dumps(segments), json.dumps(destination))
# cursor.execute(insert_stmt, data)

cursor.close()
cnx.close()