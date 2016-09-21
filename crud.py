import mysql.connector
import json
from Route import Route

class Crud():

    def __init__(self, password):
        self.password = password
        self.database = "RouteMon"

        self.cnx =  mysql.connector.connect(user='routemon', password=password, database=self.database)


    def get_routes(self, user_name=None):
        cursor = self.cnx.cursor()

        query = "SELECT * from Routes"
        if user_name:
            query = query + " where user_name =" + user_name

        cursor.execute(query)

        routes = []
        for (route_num, user_name, route_name, segments, destination) in cursor:
            route = Route(route_num=route_num, user_name=user_namem segments=segments, destination=destination)
            routes.append(route)

        cursor.close()
        return rows

    def get_routeinfos(self, user_name=None):
        cursor = self.cnx.cursor()

        query = "SELECT * from RouteInfo"
        if user_name:
            query = query + " where user_name =" + user_name

        cursor.execute(query)

        infos = []
        for (route_info_num, route_info, route_num, date_time) in cursor:
            row = {}
            row["route_info_num"] = route_info_num
            row["route_info"] = json.loads(route_info)
            row["route_num"] = route_num
            row["date_time"] = date_time
            rows.append(row)

        cursor.close()
        return infos

