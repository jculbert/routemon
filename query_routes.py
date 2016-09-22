#!/usr/bin/env python
import json
import datetime
from routeQuery import RouteQuery
from crud import Crud

apikey ='AIzaSyDuiSPpsDNUl79MvqjbQnd32MPQ2nYhfds'
routeQuery = RouteQuery(apikey)
crud = Crud("blart")

query = 'select * from Routes'
now = datetime.datetime.now()

#queries all routes in Routes table with a route info
routes = crud.get_routes()
for route in routes:

    if route.query_time > now :
        print "Valid Future Timestamp"
        routeInfo = routeQuery.query(route)
        crud.add_routeInfo(routeInfo)
        print 'Route Queried'
    else:
        print "Timestamp in Past"
        break



