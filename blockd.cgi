#!/usr/bin/python

import os,cgi,cgitb,sys,time
from commands import getstatusoutput
import MySQLdb as sql

cgitb.enable()

print "content-type:text/html"
print ""

recv=cgi.FieldStorage()

drive=recv.getvalue('d')
size=recv.getvalue('s')
platform='block'
# Open database connection
sq=sql.connect("127.0.0.1","root","anjali","adhoc")

# prepare a cursor object using cursor() method
cur=sq.cursor()

query="insert into drive (drivename,drivesize,source) values (%s,%s,%s)"
cur.execute(query,(drive,size,platform))
sq.commit()

lvcreate="sudo lvcreate  --name {} -V{}M --thin mydevice/thin".format(drive,size)
createlv=getstatusoutput(lvcreate)

l1=getstatusoutput('sudo echo    >> /etc/tgt/targets.conf')
l2=getstatusoutput('sudo echo \<target '+drive+'\>  >> /etc/tgt/targets.conf')
l3=getstatusoutput('sudo echo backing-store /dev/mydevice/'+drive+ ' >> /etc/tgt/targets.conf')
l4=getstatusoutput('sudo echo \</targets\>  >> /etc/tgt/targets.conf')
l5=getstatusoutput('sudo echo    >> /etc/tgt/targets.conf')
l6=getstatusoutput('sudo systemctl restart tgtd')


os.system('sudo echo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.1 --discover > /var/www/cgi-bin/block_discover.sh')

os.system('sudo echo iscsiadm --mode node --targetname '+drive+' --portal 192.168.122.1:3260 --login > /var/www/cgi-bin/block_login.sh')

os.system('sudo echo iscsiadm --mode node --targetname '+drive+' --portal 192.168.122.1:3260 --logout > /var/www/cgi-bin/block_logout.sh')

io=getstatusoutput("sudo tar cvf /var/www/html/block.tar block_discover.sh block_login.sh block_logout.sh")

print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1/block.tar'/>"	




