from routeQuery import RouteQuery

from route import Route

#apikey =
waypoints = []
waypoint1 = ('43.267880, -79.892870','Hamilton')
waypoint2 = ('43.526907, -80.262387','Guelph')
waypoint3 = ('43.474657, -80.546447','University of Waterloo')
waypoints.append(waypoint1)
waypoints.append(waypoint2)
waypoints.append(waypoint3)
origin = ('43.865926, -79.289759','Markville Mall')
destination = ('43.380903, -80.496452','Huron Kitchener')

route1 = Route(origin, destination , waypoints )

defineRoute= RouteQuery(route1,apikey)

routeInfo=defineRoute.query()

hello = "false"