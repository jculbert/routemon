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
    return json.dumps({"routes": routes})

def get_routeinfo(user_name=None):

    crud = Crud("blart")
    routeinfo = crud.get_routeinfo_serializable(user_name=user_name)
    return json.dumps({"routeinfo": routeinfo})

# Iterate over the request parameter key value pairs
arguments = cgi.FieldStorage()
func = None
user_name = None
for key in arguments.keys():
    if key == "func":
        func = arguments[key].value
    elif key == "user_name":
        user_name = arguments[key].value

if func == "routes":
    response = get_routes(user_name)
elif func == "routeinfo":
    response = get_routeinfo(user_name)
else:
    response = {"error": "Unrecognized function"}

print "Content-type: application/json\n\n"
print response




