import os, shutil
import time

# if os.path.isfile("dir1"):
#     shutil.rmtree("dir1")
# else:
#     pass
# os.mkdir("dir1")

# file1=open("dir1/file2.txt",'w+')
# file1.write("Salam bratandar")
# file1.close()


# file1=open("dir1/file2.txt",'r+')
# print(file1.read())
# file1.close()

# time.sleep(5) # delays for 5 seconds

#shutil.rmtree("dir1")

#os.rename("dir1","dir2")
str_test = "mirlan Tokonbekov"

a=str_test.capitalize()
print(a)


spl=str_test.split(" ")

num=enumerate(spl)

for i,v in num:
    print(i,v)

#########################
name = "Mirlan"
a=     name.__len__()
b=     len(name)
print(a,b)

number = 10
c = number.__add__(40)
print(c)

###########################

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "Vector %d, %d"%(self.a, self.b)
    
#     def __add__(self):
#         return "Vector {}, {} nerse".format(self.a, self.b)



v1 = Vector(2,4)
print(v1) 

# s=v1.__add__()
# print(s)
#############################################3

class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    # def __str__(self):
    #     return "%s is a %s" % (self.name, self.species)


a = Pet("jax", "human")
print (a.getName())

 




