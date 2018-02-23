#!/usr/bin/env python 
 
from subprocess import Popen, PIPE
import subprocess

subprocess.call(["ping", "-c 4","google.com"],stdout=open("ping.log",'w'))
os.remove("ping.log")


process = Popen(['cat', '/home/tokonbekov/src/sixonix/xonotic/install.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
# print(stdout)  

s = subprocess.check_output(["ping", "-c 4", "google.com"])
output = s.decode("utf-8")
 
lines = output.split('\n')
 
for line in lines:
    print(line)

# s = subprocess.check_output(["ping", "-c 4", "google.com"])
# output = s.decode("utf-8")
 
# lines = output.split('\n')
 
# statistics = (lines[7])
# values = statistics.split(", ")
# for v in values:
#     print(v)




    # proc = subprocess.Popen(cmd,
    #                         stderr=open(os.devnull, "w"),
    #                         stdout=subprocess.PIPE,
    #                         env=env)
    # (out, _) = proc.communicate()

    # reg = RESULT_RE.findall(out.decode())
    # m = str(reg).split(",")[0]
