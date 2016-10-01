import mysql.connector
import json
from Route import Route
from point import Point

class Crud():

    def __init__(self, password):
        self.password = password
        self.database = "RouteMon"

    def get_routes(self, user_name=None):
        cnx =  mysql.connector.connect(user='routemon', password=self.password, database=self.database)
        cnx2 =  mysql.connector.connect(user='routemon', password=self.password, database=self.database)
        cursor = cnx.cursor()

        query = "SELECT * from Routes"
        if user_name:
            query = query + " where user_name =" + user_name

        cursor.execute(query)

        routes = []
        for (route_num, user_name, route_name, points, query_time) in cursor:

            # Get the summary from the newest route_info for the route
            summary = "No summary"
            query = "SELECT summary from RouteInfo where route_num=" + str(route_num) + " order by date_time desc";
            cursor2 = cnx2.cursor()
            cursor2.execute(query)
            row = cursor2.fetchone()
            if row:
                summary = row[0]
            cursor2.fetchall() # Need to do this before calling close for some reason
            cursor2.close()

            points_list = json.loads(points)
            points = []
            for p in points_list:
                points.append(Point(name=p['name'], location=p['location']))
            route = Route(route_num=route_num, user_name=user_name, route_name=route_name, points=points, query_time=query_time, summary=summary)
            routes.append(route)

        cursor.close()
        cnx.close()
        cnx2.close()
        return routes

    def get_routes_serializable(self, user_name=None):

        routes_list = []
        routes = self.get_routes(user_name=user_name)
        for route in routes:
            routes_list.append(route.to_dict())

        return routes_list

    def get_routeinfo_serializable(self, user_name=None):
        cnx =  mysql.connector.connect(user='routemon', password=self.password, database=self.database)
        cursor = cnx.cursor()

        query = "SELECT * from RouteInfo"
        if user_name:
            query = query + " where user_name =" + user_name

        cursor.execute(query)

        infos = []
        for (route_info_num, route_num, segment_info, summary, date_time) in cursor:
            row = {}
            row["route_info_num"] = route_info_num
            row["route_num"] = route_num
            row["segment_info"] = json.loads(segment_info)
            row["summary"] = summary
            row["date_time"] = str(date_time)
            infos.append(row)

        cursor.close()
        cnx.close()
        return infos

    def add_routeInfo(self, route_info):
        cnx =  mysql.connector.connect(user='routemon', password=self.password, database=self.database)
        cursor = cnx.cursor()

        insert_stmt = "INSERT INTO RouteInfo (route_num, segment_info, summary) VALUES (%s,%s,%s)"
        data = (route_info.route_num, route_info.get_segment_info_json(), route_info.summary)
        cursor.execute(insert_stmt, data)
        cnx.commit()

        cursor.close()
        cnx.close()


