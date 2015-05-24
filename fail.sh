#!/bin/bash

count=$(cat /var/log/secure | grep -w Failed | awk '{print $11}'| sort | uniq -c | awk '{print $1}')

if [ $count -eq 3  ]
then
ip=$(cat /var/log/secure | grep -w Failed | awk '{print $11}'| sort | uniq)
iptables -A INPUT -s $ip -j DROP
fi

