def summ(*args):
    o=0
    for i in args:
        o+=i
    print(o)
summ(1,1,3,34,7)

def add_num(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add_num(1,2,333)

print("\n" * 5)
print("hi")

print("Menin atym Mirlan", end='')
print(" fiom Tokonbekov")

#nested lists

foods = ["potato", "carot", "onion", "bread", "grape", "melon"]
games = ["soccer","basketball","aakchel","regbi","chess","football"]

list1 = [foods,games]

print(list1[0][-1])

#Tuples
foods_tup = ("potato", "carot", "onion", "bread", "grape", "melon")
#foods_tup.insert(1,"ak")  cannot change Tuples
print(foods_tup)

#Set
games_set = {"soccer","basketball","aakchel","regbi","chess","football","chess","chess"} # only 1 "chess" passes
# games_set.append(1,"sa")  no append
print(games_set)

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
# print(food.items())
# print(food.keys())
# print(food.values())

for i,k in food.items():
    print(i,k )












