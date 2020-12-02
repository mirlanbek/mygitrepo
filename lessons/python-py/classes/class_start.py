# !!!!!! IMPORTANT:  

# from otherfile import TheClass
# theclass = TheClass()
# # if you want to return the output of run
# return theclass.run()  
# # if you want to return run itself to be used later
# return theclass.run

#from FOLDER_NAME import FILENAME
# from FILENAME import CLASS_NAME FUNCTION_NAME

##############################################
# Inherit from older Class

dos = "aibek"

class point(object):

    def __init__(self, at="Ainash", fio="Takanbekova"):
        self.at = at
        self.fio = fio

    def func(self):
        return "Salam bul point class function"

# p2 = point()
# print (  p2.func())

# class Onp(point):
#     def member(self):
#         return "Menin atym %s familyam %s"%(self.at, self.fio)

# p1 = Onp("Mirlan", "Tokonbekov")
# print(p1.member())


################################################ use __str__ #################
### note: if use __str__ use return, otherwise wont work #################

def func():
    return "Salam bul jon ele function"


class family:
    
    lastname = "Tokonbekov"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return (  "bizdin familyabyz %s, menin atym %s, men %d jashtamyn"%(self.lastname, self.name, self.age)  ) # here

p1 = family("Nurken", 31)

# print(p1)


################################################################################################
#333333############## start.py  tomonkunu koi:

################################################################################################
#333333############## start.py  tomonkunu koi:

# from class_start import *
# onp2 = onp("Miki","Tokonbekov")

 

# ##################################

# class family:
    
#     lastname = "Tokonbekov"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         # self.member = member()
    
#     def __str__(self):
#         return (  "bizdin familyabyz %s, menin atym %s, men %d jashtamyn"%(self.lastname, self.name, self.age) + 
#         "\n , " + o.member() + 
#         "\n , " + func() +
#         "\n , " + o.fio )# here very important "fio is veriable from different file"

# p1 = family("Nurken", 32)

# print(p1)
