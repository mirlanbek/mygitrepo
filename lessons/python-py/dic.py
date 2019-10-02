-------------  set default value to dictionary -----------------------------------

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


---------------------------------------------------------------------------------------------------------------------------------



# Dict

# classmates={"ulan":"banka zapravkada", "aibo":"jogorku keneshte jurot", "suiun":"echkim bilbeit"}

# print(classmates['ulan'])

worker1={"name": "Zabeen", "age": 27, "tel": 773122121}



print(worker1.get("tel"))

print(worker1['tel'])

print(worker1.keys())

print(worker1.values())

print(worker1['tel'])

food = {



    "name": "Mirlan",

    "age": 36,

    "tel": 12345678

}

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




