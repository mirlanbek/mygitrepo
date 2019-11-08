# ---------------------- seattr -------------

class Person():
    pass

p = Person()

key = 'name'
val = 'Miki'

setattr(p, key, val)

print(p.name)

****
output: Miki
-----------------
name = getattr(p, key)
print(name)
-----------------------------------------------
person = Person()
person_info = { 'first': 'Miki', 'last': 'Tokon' }
for key,value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

#  print(hasattr(p1, "age")) ===> True or False

-------------------------------------------------------------


class Onp:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.full = self.name + " Tokonbekov"

    def __getitem__(self, index):
        global lis
        lis = [1,2,3]
        return lis[index]

    def test(self):
        return "Menin atym %s, \
            men %d jastamyn"%(self.name,self.Nuku)

p1 = Onp("miki", 40)

callable_methods = []

methods = [  callable_methods.append(m) for m in dir(p1) if callable(getattr(p1, m))   ]

print(callable_methods)



