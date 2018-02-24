#!/bin/bash

source conf.txt

for i in $m_curr_ip $c_curr_ip ; do

scp prep.sh conf.txt $i:$script_dest

done
echo "All files are copied to target hosts"



for k in $m_curr_ip $c_curr_ip ; do

ssh $k "bash -x $script_dest/prep.sh"

done  
