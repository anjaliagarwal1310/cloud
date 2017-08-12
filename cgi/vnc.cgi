#!/usr/bin/python2

import cgi,cgitb,sys,time,commands,os
from commands import getstatusoutput

cgitb.enable()

print "content-type:text/html"
print ""


#this is to receive all values from cloud
recv=cgi.FieldStorage()

#get type of iaas
iaasc=recv.getvalue('r')

#get port no and password to connect on vnc software
port=recv.getvalue('n')
password=recv.getvalue('p')

#get osname by which client wants the new system
osname=recv.getvalue('o')

#creating image for redhat systems for iaas cloud 
image1=getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/redhat11.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(osname))

if iaasc == 'iaas1' :
	s2=('sudo virt-install --graphics vnc,listen=192.168.1.10,port={},password={} --cdrom /root/Downloads/kali-linux-2.0-amd64.iso --ram 512 --vcpu 1 --nodisk --name {}'.format(port,password,osname))
	os1=getstatusoutput(s2)

elif iaasc == 'iaas2' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={},password={} --ram 1024 --vcpu 1 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(port,password,osname,osname))

elif iaasc == 'iaas3' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={},password={} --ram 1024 --vcpu 2 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(port,password,osname,osname))

elif iaasc == 'iaas4' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={},password={} --ram 2048 --vcpu 1 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(port,password,osname,osname))

elif iaasc == 'iaas5' :
	os1=getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port={},password={} --ram 2048 --vcpu 2 --disk path=/var/lib/libvirt/images/{}.qcow2  --name {} --import --noautoconsole'.format(port,password,osname,osname))

else :
	print "wrong display"


