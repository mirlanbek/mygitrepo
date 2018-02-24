#!/bin/bash
source conf.txt

ifconfig
sleep 5


ip=`ifconfig enp0s8 | grep -w inet | awk '{print $2}'`

if [ $m_curr_ip == $ip ] ; then
	hostnamectl set-hostname $m_hostname
elif [ $c_curr_ip == $ip ]; then
	hostnamectl set-hostname $c_hostname
fi


echo "Hostname is confgured"





