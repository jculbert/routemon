import mysql.connector

class Crud():
	
	def __init__(self, password):
		self.password = password
		self.database = "RouteMon"
		
		self.cnx mysql.connector.connect(user='routemon', password=password, database=self.database)


	def getAllRoutes(self):
		cursor = cnx.cursor()
  	
		query = "SELECT route_num, user_name, route_name, origin, destination, waypoints from " + self.database

		cursor.execute(query)
	  
		cursor.close()

