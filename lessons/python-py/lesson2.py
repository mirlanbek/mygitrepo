def san():
    print("Salam dostor")

san()

def kurs(som=12):
    a=70*som
    print(a)
kurs()

def add_num(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add_num(1,2,333)

classmates={"ulan":"banka zapravkada", "aibo":"jogorku keneshte jurot", "suiun":"echkim bilbeit"}

del classmates["ulan"]                # del dict
classmates["ulan"] = "sd"             # update dict

classmates.update({"tico": "men"})    # list append using update
for i,k in classmates.items():
    print(i,k)

print(classmates['aibo'])
print(len(classmates))


# with open("file2.txt",'r+') as a:
#     print(a.read())

# $$$$$$$$$$$$$$$$$$  vars([x])  $$$$$$$$$$$$$$$$$

from timeit import timeit


e=timeit('object.__dict__;object.__dict__')
print (e)

w=timeit('vars(object);vars(object)')
print(w)





