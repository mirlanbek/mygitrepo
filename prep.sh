#!/bin/bash

source conf.txt

iptables -F

ip=`ifconfig enp0s8 |grep -w inet | awk '{print $2}'`

if [ $ip == $m_currip ] ; then
hostnamectl set-hostname nismaster
elif [ $ip == $c_currip ] ; then
hostnamectl set-hostname nisclient
fi
echo "hostnames are set"
nisdomainname osh.kg
h=`hostname`

if [ $h == nismaster ] ; then
cat > /etc/sysconfig/network-scripts/ifcfg-enp0s9<<EOF
BOOTPROTO=static
DEVICE=enp0s9
ONBOOT=yes
IPADDR=$m_newip
NETMASK=255.255.255.0
EOF

elif [ $h == nisclient ] ; then
cat > /etc/sysconfig/network-scripts/ifcfg-enp0s9<<EOF
BOOTPROTO=static
DEVICE=enp0s9
ONBOOT=yes
IPADDR=$c_newip
NETMASK=255.255.255.0
EOF
fi
ifdown enp0s9
ifup enp0s9
echo "new ip is set"
sleep 2
cat > /etc/hosts<<EOF

localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.56.103 server1 s1
192.168.56.10  nismaster m1
192.168.56.11  nisclient c1
EOF
echo "dns is set"
sleep 2
yum install rpcbind ypserv yp-tools ypbind -y

cat > /etc/yp.conf<<EOF
ypserver nismaster
domain osh.kg
EOF
 
sleep 2

systemctl start rpcbind ; systemctl enable rpcbind
if [ $h == nismaster ] ; then
systemctl start ypserv ; systemctl enable ypserv
systemctl start ypxfrd
fi

sleep 2

sed -i 's/passwd:   files/passwd: nis files/g' /etc/nsswitch.conf
sed -i 's/shadow:   files/shadow: nis files/g'  /etc/nsswitch.conf
sed -i 's/group:    files/group: nis   files/g' /etc/nsswitch.conf

if [ $h == nismaster ] ; then
/usr/lib64/yp/ypinit -m
elif [ $h == nisclient ] ; then

usr/lib64/yp/ypinit -s nismaster
fi

systemctl start ypbind ; systemctl enable ypbind
sleep 2


echo "all done"
