from routeQuery import RouteQuery
from segment    import Segment
from Route import Route
import json
from json import JSONEncoder


segments = []

segment = Segment('43.865926, -79.289759','Markville Mall')
segments.append(segment)
segment = Segment('43.267880, -79.892870','Hamilton')
segments.append(segment)
segment = Segment('43.526907, -80.262387','Guelph')
segments.append(segment)
segment = Segment('43.474657, -80.546447','University of Waterloo')
segments.append(segment)
destination = ('43.380903, -80.496452','Huron Kitchener')
route1 = Route(segments,destination )
print(route1)


apikey = 'AIzaSyDuiSPpsDNUl79MvqjbQnd32MPQ2nYhfds'



routeQuery= RouteQuery(route1,apikey)

routeInfo=routeQuery.query()
print (routeInfo.to_JSON())


hello = "false"



