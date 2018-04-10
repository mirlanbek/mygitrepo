#!/bin/bash


iptables -F
Hello!
Hello!
Hello!

How are you doing?
How are you doing?
How are you doing?
#   $0   filename je ./filename
#   $1   2- position
#   $2   3-position

case $1 in

"-s") echo "suuga bar"   ;;
"-a") echo "aiga bar" ;;
"") echo  " E ketip kalchy"   ;;
*) echo "e jakshyna soz kirgiz"

esac

if [  $1 ]; then
echo then
fi



venera(){
echo "Salam, sen azyr $1 menen $2tin ichin kara"
cat $1 

cat $2
}


venera  /etc/fstab start.sh 



















