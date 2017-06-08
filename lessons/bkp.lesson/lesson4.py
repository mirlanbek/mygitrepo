# Class

# class enemy():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def attack(self):
#         print("{} attacks which is {} let".format(self.name,self.age))
    
 
# p1=enemy("Niki",23)
# p2=enemy("Nuku",25)

# p1.attack()
# p2.attack()  

class enemy():

    count=12

    def __init__(self, name="Nuku", age=25):
        self.name = name
        self.age = age

    def attack(self):
        print("{} attacks which is {} let, baary {}".format(self.name,self.age,enemy.count))


p1=enemy("Aibek",43)
p2=enemy()
     
  
p2.attack()
p1.attack()

class employee():

    lastname = "Tokonbekov"

    def __init__(self,name='Mirlan',age=37):
        self.name = name
        self.age = age
        
    
    def onp(self):
        print("Bizdin baarybyzdyn familyabyz {}, atym  bolso {}, jashym {} jashta".format(employee.lastname,self.name,self.age))

emp1 = employee("Nurken",23)
emp2=employee()

emp1.onp()
emp2.onp()

#!/usr/bin/env python

class family ():
    lastname = "Tokonbekov"

    def __init__(self, name,age):
        self.name=name
        self.age=age

    def member(self):
        return "Bizdin baarybyzdyn familyabyz {}, atym {} jana men {} jashtamyn".format(family.lastname,self.name,self.age)
    
member1=family("Mirlan",37)

print(member1.member())

print(family.member(member1), family.lastname )


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

print(p1.member())
################################################ use __str__ #################
### note: if use __str__ use return, otherwise wont work #################
class family:
    
    lastname = "Tokonbekov"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return (  "bizdin familyabyz %s, menin atym %s, men %d jashtamyn"%(self.lastname, self.name, self.age)  ) # here

p1 = family("Nurken", 31)

print(p1)
