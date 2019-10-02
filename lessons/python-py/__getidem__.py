
param={"men": "sen"}  

class Hero(object):

    def __getitem___(self,key):
        return param[key]

p1 = Hero()
print(p1['men'])

# ----------------------

ascii_letters="Mirlan"

class MyContainer(object):
    def __getitem__(self, key):
        return ascii_letters[key]           #  __getitem__ we need it when we pass indexing itself like here 


my_container = MyContainer()  
print(my_container[1:])
 
 
# --------------------------------------------------------



from string import ascii_letters

class MyContainer(object):

    def __getitem__(self, key):
        return ascii_letters[key]           #  __getitem__ we need it when we pass indexing itself like here 


my_container = MyContainer()  

print(ascii_letters[5])
print(my_container[0])  # a
print(my_container[16])  # q



#------------------------------------------------------

class CustomList(object):
    def __init__(self, elements=0):
        self.my_custom_list = [0] * elements

    def __setitem__(self, index, value):
        self.my_custom_list[index] = value

    def __getitem__(self, index):
        return "Hey you are accessing {} element whose value is: {}".format(index, self.my_custom_list[index])

    def __str__(self):
        return str(self.my_custom_list)

obj = CustomList(12)
obj[0] = 1
print(obj[0])
print(obj)


# ----------------------------------------------------




