import os
import sys
import argparse

help="""
ERROR: please check USAGE:

# USAGE: 
#  python3 ping.py -i ips.txt -o my_output.txt

"""   
parser = argparse.ArgumentParser(description="ip ping checker")
parser.add_argument("-i", "--ips", type=str, help="filename for list of hostnames or ips need to be checked")
parser.add_argument("-o", "--output", type=str, help="provide desired output file name, default is output.txt")
args=parser.parse_args()

output_file="output.txt"

if args.output:
    output_file = args.output

if args.ips:
    hostfile = args.ips
else:
    exit(help)




my_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(my_dir)
if os.path.exists(output_file):
    os.system(f"rm -rf {output_file}")

global active
active=[]

global unreachable
unreachable=[]



def check(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        active.append(hostname)
    else:        
        unreachable.append(hostname)
    return 

 
def check_ping(hostfile):

    with open(hostfile, "r") as hf:
        for host in hf.read().split():
            check(host.strip())
            
    with open(output_file, "a+") as w:
        w.write("Active Systems:")

        for i in active:
            w.write("\n\t"+i)
            
        w.write("\n\n\n Unreachible Systems:")
        for k in unreachable:
            w.write("\n\t"+k)
    return 




if __name__ == '__main__':
    check_ping(hostfile)
