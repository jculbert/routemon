import cgi
import cgitb; cgitb.enable() # Optional; for debugging only

print "Content-type: text/html\n\n"
print "<html>Routemon home page</html>"

#arguments = cgi.FieldStorage()
#for i in arguments.keys():
#    print arguments[i].value
