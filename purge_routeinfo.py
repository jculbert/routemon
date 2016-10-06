#!/usr/bin/env python

import datetime
from crud import Crud

purge_before_time = datetime.datetime.now() - datetime.timedelta(2)
date_str = purge_before_time.strftime("%Y-%m-%d")

print "Purgeing routeinfo older than " + date_str

crud = Crud("blart")
crud.purge_routeinfo(older_than_date_str=date_str)

