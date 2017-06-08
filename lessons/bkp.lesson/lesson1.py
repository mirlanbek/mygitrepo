foods = ["potato", "carot", "onion", "bread", "grape", "melon"]
name = """Menin atyn 
Mirlan"""
lastname = " Tokonbekov"
a = (name[13:] + lastname[:-1])
print(a)

foods.append("kartoshko")
foods.remove("potato")

for i in foods[:2]:
    print(i)

for i in range(10):
    if i == 5:
        continue
    elif i == 6:
        break
    else:
        print (i," Mika")

b=1

while b < 1:
    print("mika")
    b+=1

print(foods)

foods.insert(1,"sabiz")
foods.remove("onion")
del foods[5]
foods.sort()
foods.reverse()
foods.append("shakar")
print(max(foods))
print(min(foods))
print(len(foods))
print(foods)
a=list()
dir(a)