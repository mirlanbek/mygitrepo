import sys, os

from path import Project_Map

a = Project_Map("Miki.conf")
b = a.root_path()








class point():
    def __init__(self, at, fio):
        self.at = at
        self.fio = fio

class onp(point):
    def member(self):
        return "Menin atym %s familyam %s"%(self.at, self.fio)



class family2:
    lastname = "Tokonbekov"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return (  "bizdin familyabyz %s, menin atym %s, men %d jashtamyn"%(self.lastname, self.name, self.age)  ) # here


# # world/africa/__init__.py  (Empty file)

# # world/africa/zimbabwe.py
# print("Shona: Mhoroyi vhanu vese")
# print("Ndebele: Sabona mhlaba")

# # world/europe/__init__.py
# from . import greece
# from . import norway

# # world/europe/greece.py
# print("Greek: Γειά σας Κόσμε")

# # world/europe/norway.py
# print("Norwegian: Hei verden")

# # world/europe/spain.py
# print("Castellano: Hola mundo")

# # world/__init__.py
# from . import africa