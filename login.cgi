#!/usr/bin/python2

import cgi,cgitb,sys,time,commands,os
import MySQLdb as sql

cgitb.enable()

print "content-type:text/html"
print ""

#this is to receive username and password from cloud

recv=cgi.FieldStorage()

#used to get user and password for login
userl=recv.getvalue('unamel')
passwordl=recv.getvalue('pswl')

#used to select button for login or signup
button1=recv.getvalue('login')
button2=recv.getvalue('signup')

#used to get user and password to add new user
users=recv.getvalue('unames')
passwords=recv.getvalue('psws')
passwordr=recv.getvalue('psw-repeat')

# Open database connection
sq=sql.connect("127.0.0.1","root","anjali","adhoc")

# prepare a cursor object using cursor() method
cur=sq.cursor()

if userl != None :
	query="select * from user where username=%s and password=%s"
	cur.execute(query,(userl,passwordl))
	if cur.rowcount == 1:
		print "<META HTTP-EQUIV='refresh' content='0; url=/services.html'/>"

	else:
		print "<script>alert('Wrong USERNAME or PASSWORD')</script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=/log.html'/>"


elif passwords == passwordr :
	query="insert into user (username,password) values (%s,%s)"
	cur.execute(query,(users,passwords))
	sq.commit()
	print "<script>alert('SIGNUP succesfull!! NOW LOGIN')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/log.html'/>"


else :
	print "<script>alert('Passwords do not match')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/log.html'/>"


sq.close()

