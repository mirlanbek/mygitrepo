#!/usr/bin/python3

import os
import sys

# USAGE:
#  python3 ping.py ips.txt | tee -a output.txt



def check(hostname):
   response = os.system("ping -c 1 " + hostname)
   # and then check the response...
   if response == 0:
       pingstatus = hostname +" is Active"
   else:
       pingstatus = hostname +" is Unreachable"

   return pingstatus




def check_ping(hostfile):
   with open(hostfile, "r") as hf:
       for host in hf.read().split():
           print(check(host.strip()))

   return


if __name__ == '__main__':
   print(check_ping(sys.argv[1]))
