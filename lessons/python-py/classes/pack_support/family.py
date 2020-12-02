import sys, os

from path import Project_Map 

# import path  

# from game import game_enemy

# if __name__=="__main__":
#     sys.path.append(os.path.dirname(os.path.abspath(sys.argv[0])))
# from . import Project_Map

a = Project_Map(r="Miki")
b = a.root_path()
print (a.root_path())



# c = path.Project_Map().root_path()


# print (c)


# class family ():
#     lastname = "Tokonbekov"

#     def __init__(self, name,age):
#         self.name=name
#         self.age=age

#     def member(self):
#         return "Bizdin baarybyzdyn familyabyz {}, atym {} jana men {} jashtamyn, secretnye fily: {}".format(family.lastname,self.name,self.age, self.b)
    
# member1=family("Mirlan",37)
# print(member1.member())
# print(member1.member())

# print(family.member(member1), family.lastname )


##############################################
# Inherit from older Class

class point():

    def __init__(self, at, fio):
        self.at = at
        self.fio = fio

class onp(point):
    def member(self):
        return "Menin atym %s familyam %s"%(self.at, self.fio)
p1 = onp("Mirlan", "Tokonbekov")

#print(p1.member())
################################################ use __str__ #################
### note: if use __str__ use return, otherwise wont work #################
class family2:
    
    lastname = "Tokonbekov"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return (  "bizdin familyabyz %s, menin atym %s, men %d jashtamyn"%(self.lastname, self.name, self.age)  ) # here

# p1 = family("Nurken", 31)

# print(p1)
