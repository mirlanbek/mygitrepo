import sys, string
# a=sys.path.append(path.join(path.dirname(path.abspath(sys.argv[0])), ".."))

Tokonbekov=("Mirlan", "Nurken", "Suiun", "Ainash")
# name = raw_input("Enter your name: ")
name = "Suiun"
a= string.digits[2]

for i in Tokonbekov:
    if i == Tokonbekov[int(a)]:
        break
    else:
         print(i) 

########################################

import os, os.path
print(os.__file__)
os.chdir("newdir")
print( os.getcwd())

with open(os.getcwd()+"/first.py", "r+") as a:
    e=a.read()

filePath = os.getcwd()+"/first.py"


dirs = 'file1', 'file2','file3'

print(os.path.join('dir1','dir2'))
print(  os.path.split(filePath)   )
print( os.path.basename(filePath)   )


zb=os.stat(filePath).st_size
print(zb)

print(os.path.abspath(filePath))

###############################################


if os.path.exists("dir1/dir2/dir3"):
    pass
else:
    os.makedirs("dir1/dir2/dir3")

f1 = open("dir1/dir2/dir3/file1","w+")
f1.write("Salambul file1din ichi")
f1.close()
print(f1.closed)

newpath = os.getcwd()+"/dir1/dir2/dir3/file1"
n1 = os.path.dirname(newpath)
print(n1)

n2=os.path.basename(newpath)
print(n2)

n3= os.path.split(newpath)
print(n3)

print (os.path.join(n1,n2))

print(  type(f1)  )



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

# ============================================================================================= 


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

# =================================================

import os, shutil
import time

if os.path.isfile("dir1"):
    shutil.rmtree("dir1")
else:
    pass
os.mkdir("dir1")

file1=open("dir1/file2.txt",'w+')
file1.write("Salam bratandar")
file1.close()


file1=open("dir1/file2.txt",'r+')
print(file1.read())
file1.close()

time.sleep(5) # delays for 5 seconds

shutil.rmtree("dir1")

os.rename("dir1","dir2")