import xml.etree.ElementTree as ET

f_xml="/home/tokonbekov/dir/learn/python-test/lessons/dir_2/books.xml"
 
x = ET.parse(f_xml)
tests = x.findall("testsuites/testcase")        


 

# tests = x.findall("FOREST/TREE")        
for i in tests:
    print(i.text)

for test in tests:
    option = test.attrib['name']

for test1 in tests:
    option2 = test1.attrib['time']
opt2=str(option2)

print(type(opt2))
# print ( option)
#option2 = tests.attrib['time']


print(    "Bizdin mekteptin aty %s, sabak %s saatan kiyin bashtalat"%(option,opt2)      )

# test_names_suffix = [test.attrib["classname"] + "." + test.attrib["name"] for test in tests]
# test_names = [".".join(test.split(".")[:-1]) for test in test_names_suffix]

 