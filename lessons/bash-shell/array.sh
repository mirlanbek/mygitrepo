#!/bin/bash
array=("bir" "eki" "uch" 7)

#if [[ " ${array[@]} " =~ " ${value} " ]]; then
if [[ " ${array[@]} " =~ "uch" ]]; then
echo bar  
array+=(8)

echo ${array[@]}

aa=` expr ${#array[@]} - 1` 
echo ${array[$aa]} 
   # whatever you want to do when arr contains value
fi

if grep -q rr test.sh ;then
echo bar eken
fi

