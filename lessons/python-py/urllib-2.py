import os
import sys
import urllib2
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))
# import build_support as bs
import xml.etree.ElementTree as et


url = "http://otc-mesa-ci.jf.intel.com/computer/api/xml"
print ("opening: " + url)
f_xml=urllib2.urlopen(url)
x = et.parse(f_xml)

def is_excluded():
    if ("builder" in hosts or hosts == "master"):
        return True

tests = x.findall("computer/displayName")        
for host in tests:
    hosts = host.text
    if is_excluded():
        continue
    print(hosts)
