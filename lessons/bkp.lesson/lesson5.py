import os,shutil

if  os.path.isfile("test_bir"):
    shutil.rmtree("test_bir")

if not os.path.isfile("test_bir"):
    os.mkdir("test_bir")

fw = open("test_bir/file.txt",'w+')
fw.write("Salam de")
fw.close()
print(fw.name,fw.mode, fw.closed)

rf = open("test_bir/file.txt",'r')
a=rf.read()
print(a)


from start import main 
main()

import os,os.path,shutil



if os.path.exists("dir1"):
    pass
else:
    os.makedirs("dir1")
    print("dir degen papka tuzdum")


with open ("dir1/file1","w+") as f1:
    f1.write("Salam bizdin tuugadar,  kandaisynar?")

with open("dir1/file1", "r+") as f2:
    print(   f2.read()    ) 

try:
    shutil.rmtree("dir1")
    print("papkan ketti")
except Exception as bobo:
    print("Bobodu: ",bobo)

