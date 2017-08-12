#!/usr/bin/python2

import cgi,cgitb,sys,time,commands,os
from commands import getstatusoutput
from random import randint

cgitb.enable()

print "content-type:text/html"
print ""

#port=randint(5900,6000)


#this is to receive which service is required in paas cloud
recv=cgi.FieldStorage()
paas=recv.getvalue('p')

#os=getstatusoutput('sudo docker run -itd -p   {}:4200 ruby_python'.format(port))
os=getstatusoutput('sudo docker start 5e3c6b418e78')

if paas == 'python' :	
	print "<a href='http://172.17.0.2:4200'>"
	print "username is user1 and password is 123 to start coding"
	print "</a>"

elif paas == 'ruby' :
	print "<a href='http://172.17.0.2:4200'>"
	print "username is user2 and password is 123 to start coding"
	print "</a>"

elif paas == 'perl' :
	print "<a href='http://172.17.0.2:4200'>"
	print "username is user3 and password is 123 to start coding"
	print "</a>"

