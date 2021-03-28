#!/bin/bash
#salam bul test for fetch
network=5
# net=(br-ens786f1 br-ens786f2 br-ens786f3 br-ens786f4 br-ens786f5 br-ens786f6)
net1=ens786f1
net2=ens786f2
net3=ens786f3
net4=ens786f4
net5=ens786f5
net6=ens786f6
net7=ens786f7
net8=ens786f8
net9=ens786f9
net10=ens786f10
net11=ens786f11
net12=ens786f12
net13=ens786f13
net14=ens786f14
net15=ens786f15
net16=ens786f16
net17=ens786f17
net18=ens786f18
net19=ens786f19
net20=ens786f20

vilan_range=(0 1000:1100 1101:1200 1201:1300 1301:1400 1401:1500 1501:1600 1601:1700 1701:1800)

bridge (){
if [[ $network == 5 ]]
then
a=20
for i in `seq $a`
do
eval "temp=\${net$i}"
#eval "temp_range=\${vlan_range[$i]}"

#echo -n "physnet$i:br-$temp" 
printf  "%s,"  "physnet$i:br-$temp"
#printf "%s," "physnet$i:$temp_range" 
#echo ${net[@]/%/$i}
done 
printf "\n"

fi
}
bridge
#sed -i '/OVS_PHYSICAL_BRIDGE=/a \OVS_CHIK='$(bridge)'' local.conf





















