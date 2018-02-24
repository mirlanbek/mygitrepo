#!/bin/bash
source config.txt
source functions_nis

#Configure hostnames

get_ip=$(ifconfig enp0s8|awk {'print $2'}| sed -n 2p)

if [[ $get_ip == $mas_curr_ip ]];then
   hostnamectl set-hostname $mas_hostname

elif [[ $get_ip == $cl_curr_ip ]];then

   hostnamectl set-hostname $cl_hostname
fi

echo "hostname configuration is done"


#Configure DNS


cat > /etc/hosts << EOF
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
$mas_ip $mas_hostname
$cl_ip $cl_hostname

EOF

echo "done DNS configurfation"

#Set IP address

if [[ $get_ip == $mas_curr_ip ]];then

cat > /etc/sysconfig/network-scripts/ifcfg-enp0s8 << EOF
DEVICE=enp0s8
BOOTPROTO=static
ONBOOT=yes
IPADDR=$mas_ip
NETMASK=255.255.255.0
EOF
restart_network

elif [[ $get_ip == $cl_curr_ip ]];then

cat > /etc/sysconfig/network-scripts/ifcfg-enp0s8 << EOF
DEVICE=enp0s8
BOOTPROTO=static
ONBOOT=yes
IPADDR=$cl_ip
NETMASK=255.255.255.0
EOF
restart_network

fi

echo "DONE ip address set"

ifup enp0s3

install_nis (){

        if [[ $(hostname) == "nismaster" ]]; then

                yum install -y rpcbind ypserv yp-tools ypbind vim net-tools

        elif [[ $(hostname) == "nisclient" ]] ; then

                yum install -y rpcbind  yp-tools ypbind vim net-tools
        fi

}

# Configure NIS

install_nis

start_rpcbind 


if [[ $(hostname) == "nismaster" ]]; then
	start_ypserv
	systemctl start ypxfrd;systemctl enable ypxfrd
	/usr/lib64/yp/ypinit -m 
        systemctl restart ypserv
        echo "NISMASTER config is done"

fi

#Configure Nis client

cat >> /etc/yp.conf << EOF

ypserver $mas_hostname
domain $domain
EOF
 
sed -i 's/passwd: /passwd:  nis/' /etc/nsswitch.conf 

sed -i 's/shadow: /shadow:  nis/' /etc/nsswitch.conf 

sed -i 's/group: /group:  nis/' /etc/nsswitch.conf 

if [[ $(hostname) == "nisclient" ]]; then

	iptables -F

	start_ypbind

        ypcat passwd

echo "NIS client is set, uraa!"
fi
	














