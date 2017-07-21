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

os.chdir("newdir")
#print( os.getcwd())

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


# if os.path.exists("dir1/dir2/dir3"):
#     pass
# else:
#     os.makedirs("dir1/dir2/dir3")

# f1 = open("dir1/dir2/dir3/file1","w+")
# f1.write("Salambul file1din ichi")
# f1.close()
# print(f1.closed)

# newpath = os.getcwd()+"/dir1/dir2/dir3/file1"
# n1 = os.path.dirname(newpath)
# print(n1)

# n2=os.path.basename(newpath)
# print(n2)

# n3= os.path.split(newpath)
# print(n3)

# print (os.path.join(n1,n2))

# print(  type(f1)  )



