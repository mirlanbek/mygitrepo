
# Dict

classmates={"ulan":"banka zapravkada", "aibo":"jogorku keneshte jurot", "kiyal":"echkim bilbeit"}
print(classmates['ulan'])

worker1={"name": "Zabeen", "age": 27, "tel": 773122121}

print(worker1.get("tel"))
print(worker1['tel'])

print(worker1.items())
print(worker1.keys())
print(worker1.values())

food = {

    "name": "Mirlan",
    "age": 36,
    "tel": 12345678
}

print(food.items())
print(food.keys())
print(food.values())

for i,k in food.items():
    print(i,k )


--------------------------------------------  more advanced -----------------------

# -------------  set default value to dictionary -----------------------------------

#dictionary = {"message": "Hello, World!"}              

dictionary={}

data = dictionary.get("message", "i'm default value")   # Note here:  "message" has default value "i'm default value",you'll get default value until you set new

print(data)




---------------------- NOTE: dictionary creates dict randomly, that is why we need collections.OrderedDict() see below   -------------------------------------------------

import collections

dicc = {
    '/dev/sda4': 'start=129583104,size=20971520,type=0657FD6D-A4AB-43C4-84E5-0933C84B4F4F,uuid=284D59E0-6816-4F7C-ABE3-2EBAE51706BE', 
    '/dev/sda1': 'start=2048,size=1048576,type=C12A7328-F81F-11D2-BA4B-00A0C93EC93B,uuid=B6A6BDE7-F76C-48F5-AA05-4276ECE6AA61,name="EFISystemPartition"', 
    '/dev/sda2': 'start=1050624,size=4194304,type=EBD0A0A2-B9E5-4433-87C0-68B6B72699C7,uuid=0873E9DE-8663-487F-A0AC-DBE870F39326', 
    '/dev/sda3': 'start=5244928,size=124338176,type=EBD0A0A2-B9E5-4433-87C0-68B6B72699C7,uuid=623B428D-6782-488C-915F-F8243E4B48BD'}

dic=dicc.items()        # ---------- list
tmp_sda4 = dic[0]
del dic[0]
dic.insert(3,tmp_sda4)   # --------- list 

a=collections.OrderedDict(dic)

print(a.items())


# BUL eki stringden 1 dctionery jasait

import collections

val_key = "eki"
vak_val = "2"
disk_sw = collections.OrderedDict()

dicc = {}

disk_sw[val_key] = vak_val

dicc.update(disk_sw)

print(dicc)


---------------------------------------------------------------------------------------------------------------------------------



# Dict

classmates={"ulan":"banka zapravkada", "aibo":"jogorku keneshte jurot", "shukur":"bishkekte eken"}
classmates2={"miki":"budalykta", "doku":"bishkekte jurot", "jamshut":"KPSSke ui salyp atat"}

classmates.update(classmates2)
print(classmates)  # eki dict koshulat

# print(classmates['ulan'])


# ---------------- del and pop() are same  both remove dict-------------------------------------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
print(thisdict)

del thisdict["model"]
print(thisdict)

# -------------------------------------------------------------------------------------
thisdict.clear()
print(thisdict)

del thisdict     #--------------------------- remove whole dict

# --------------------------------------------------------------------
mydict = thisdict.copy()
print(mydict)




# ************************* 888888888888888888888888

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

# ************************* 888888888888888888888888

import collections

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mashina = {"type": "SUB"}

car.update({"color": "White"})
print(car)
car.update(mashina)

a="Name"
b="Mirlan"

coll = collections.OrderedDict()
coll[a] = b
car.update(coll)
print(car)
