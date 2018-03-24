#!/bin/bash

source conf.txt

for i in $m_currip $c_currip
do
scp conf.txt prep.sh $i:$dest
ssh $i  'bash -x  prep.sh'
done

