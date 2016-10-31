#!/usr/bin/python

import sys
import json
import cgi
import cgitb; cgitb.enable() # Optional; for debugging only
import datetime

sys.path.insert(0, '../routemon')
from crud import Crud

# class JSONEncoderExtended(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.isoformat()
#         elif isinstance(obj, datetime.date):
#             return obj.isoformat()
#         elif isinstance(obj, datetime.timedelta):
#             return (datetime.datetime.min + obj).time().isoformat()
#         else:
#             return json.JSONEncoder.default(self, obj)


def get_routes(user_name=None):
    crud = Crud("blart")
    routes = crud.get_routes_serializable(user_name=user_name)
    return json.dumps(routes)

def get_routeinfo(user_name=None):

    crud = Crud("blart")
    routeinfo = crud.get_routeinfo_serializable(user_name=user_name)
    return json.dumps({"routeinfo": routeinfo})

# Iterate over the request parameter key value pairs
user_name = None
response = get_routes(user_name)

print "Content-type: application/json"
print "Access-Control-Allow-Origin: http://localhost:63342\n"
print response




