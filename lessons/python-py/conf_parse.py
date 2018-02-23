import xml.etree.ElementTree as ET
import os,sys
import ConfigParser

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))

# xml_file = "dir_2/books.xml"
# x = ET.parse(xml_file)
# tests = x.findall("testsuites/testcase")        
# print([i.attrib['name']+":"+ i.attrib['classname']  for i in tests] )

x = ConfigParser.ConfigParser()
x.read("/home/tokonbekov/dir/learn/python-test/lessons/practice1/short.ini")


print(  x.get("book","title")   )
print(   x.items("book")[0]   )

# for s  in x.sections():
#     print(s)

# for o in x.options("book"):
#     print(o)

x.remove_option("book", "author")
print(   x.items("book")   )

###++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ff="/home/tokonbekov/dir/learn/python-test/lessons/bkp_lesson/miki2.conf"
# x = ConfigParser.ConfigParser()
# x.read("/home/tokonbekov/dir/learn/python-test/lessons/bkp_lesson/miki.conf")
# sections = x.sections()

# for o in x.items("expected-failures"):
#     if o[1] == "mesa a455f594bb6af2b2d8b61775c3774667db15c4a7":
#         x.remove_option("expected-failures",o[0])
#         x.write(open(ff,"w"))     

###################################++++++++++++++++++++++++++