#!/usr/bin/python

import os,cgi,cgitb,sys,time
from commands import getstatusoutput
import MySQLdb as sql

cgitb.enable()

print "content-type:text/html"
print ""

recv=cgi.FieldStorage()

#get the storage type for staas cloud (object or block) and ask for drive name and size

drive=recv.getvalue('d')
size=recv.getvalue('s')
platform=recv.getvalue('p')

# Open database connection
sq=sql.connect("127.0.0.1","root","anjali","adhoc")

# prepare a cursor object using cursor() method
cur=sq.cursor()

query="insert into drive (drivename,drivesize,source) values (%s,%s,%s)"
cur.execute(query,(drive,size,platform))
sq.commit()

if platform == 'Linux' :
	lvcreate="sudo lvcreate  --name {} -V{}M --thin mydevice/thin".format(drive,size)
	createlv=getstatusoutput(lvcreate)
	formatlv='sudo mkfs.ext4 /dev/mydevice/'+drive
	lvformat=getstatusoutput(formatlv)
	os.system('sudo mkdir /mnt/'+drive)
	os.system('sudo mount /dev/mydevice/'+drive+' /mnt/'+drive)
	x=getstatusoutput("sudo echo /mnt/"+drive+" *'(rw,no_root_squash)' >> /etc/exports")
	os.system('sudo systemctl restart nfs-server')
	os.system('sudo systemctl enable nfs-server')
	y=getstatusoutput("sudo echo mkdir /media/"+drive+ " > /var/www/cgi-bin/st.sh")
	z=getstatusoutput("sudo echo mount 192.168.122.1:/mnt/"+drive+" /media/"+drive+" >> /var/www/cgi-bin/st.sh")
	io=getstatusoutput("sudo tar cvf /var/www/html/st.tar st.sh")
	print "<META HTTP-EQUIV='refresh' content='0; url=/st.tar'/>"	
	""" check=os.system('sudo exportfs -ar')
	if check == 0 :
		print "done"  
	"""


elif platform == 'Windows' :
	lvcreate="sudo lvcreate  --name {} -V{}M --thin mydevice/thin".format(drive,size)
	createlv=getstatusoutput(lvcreate)
	formatlv='sudo mkfs.xfs /dev/mydevice/'+drive
	lvformat=getstatusoutput(formatlv)
	os.system('sudo mkdir /'+drive)
	os.system('sudo mount /dev/mydevice/'+drive+' /'+drive)
	line1=('sudo echo    >> /etc/samba/smb.conf')
	line2=('sudo echo ['+drive+'] >> /etc/samba/smb.conf')
	line3=('sudo echo path=/'+drive+' >> /etc/samba/smb.conf')
	line4=('sudo echo valid users=anj >> /etc/samba/smb.conf')
	line5=('sudo echo writable=yes >> /etc/samba/smb.conf')
	line6=('sudo echo browseable=yes >> /etc/samba/smb.conf')
	line7=('sudo echo    >> /etc/samba/smb.conf')

	cmd1=getstatusoutput(line1)
	cmd2=getstatusoutput(line2)
	cmd3=getstatusoutput(line3)
	cmd4=getstatusoutput(line4)
	cmd5=getstatusoutput(line5)
	cmd6=getstatusoutput(line6)
	cmd7=getstatusoutput(line7)
	os.system('sudo systemctl restart smb')
	cli=("sudo echo mount -o username=anj //192.168.122.1/"+drive+" /mnt/ > /var/www/cgi-bin/samba.sh")
	cli1=getstatusoutput(cli)
	io=getstatusoutput("sudo tar cvf /var/www/html/samba.tar samba.sh")
	print "<META HTTP-EQUIV='refresh' content='0; url=/samba.tar'/>"	
	

else :
	print "<script>alert('Incorrect Selection')</script>"


