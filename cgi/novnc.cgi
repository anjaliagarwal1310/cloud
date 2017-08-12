#!/usr/bin/python2

import cgi,cgitb,sys,time,commands,os
from commands import getstatusoutput
from random import randint

cgitb.enable()

print "content-type:text/html"
print ""

portu=randint(5900,6000)

#this is to receive username and password from cloud

recv=cgi.FieldStorage()

iaasc=recv.getvalue('r')
port=recv.getvalue('n')
osname=recv.getvalue('o')

#creating image for redhat systems for iaas cloud 
image1=getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/redhat11.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(osname))

if iaasc == 'iaas1' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={} --cdrom /root/Downloads/kali-linux-2.0-amd64.iso --ram 512 --vcpu 1 --nodisk --name '+osname+' --noautoconsole '.format(portu))
	print os1
	
elif iaasc == 'iaas2' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={}  --ram 1024 --vcpu 1 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(portu,osname,osname))

elif iaasc == 'iaas3' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={}  --ram 1024 --vcpu 2 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(portu,osname,osname))

elif iaasc == 'iaas4' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={}  --ram 2048 --vcpu 1 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(portu,osname,osname))

elif iaasc == 'iaas5' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={}  --ram 2048 --vcpu 2 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(portu,osname,osname))

else :
	print "wrong display"



os.system('sudo websockify -D --web=/usr/share/novnc {} 192.168.122.1:{}'.format(port,portu))	
print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1:{}'/>".format(port)


