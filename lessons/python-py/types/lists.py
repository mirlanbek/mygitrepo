list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


foods = ["potato", "carot", "onion", "bread", "grape", "melon"]
dir(foods)
ops = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

for i in foods[:2]:
    print(i)

foods.append("kartoshko")
foods.insert(1,"sabiz")

foods.sort()
foods.reverse()

foods.remove("onion")
del foods[5]
foods.pop(-1)

f=foods.copy()  # copy foods to f
f.clear()
del f

foods.count("melon")    # counts how many 'melon' in foods

fruits = ['apple', 'cherry', 'berry']
foods.extend(fruits)           # or
foods = foods + fruits


print(max(foods))
print(min(foods))
print(len(foods))
print(foods)

a=list()
dir(a)



############################


a = []

a=a+[

"mirlan",
"miki",
"tico",
"mirlanbek",
"adykovich",
"tokonbekov"


]
b=[

"kartoshka",
"sabiz",
"piyaz"

]
c = a + b 
print(c)



#nested lists

foods = ["potato", "carot", "onion", "bread", "grape", "melon"]
games = ["soccer","basketball","aakchel","regbi","chess","football"]

list1 = [foods,games]

print(list1[0][-1])


# ------------------------------------------------------------------------

Sr.No.	Function with Description
1	cmp(list1, list2)
Compares elements of both lists.

2	len(list)
Gives the total length of the list.

3	max(list)
Returns item from the list with max value.

4	min(list)
Returns item from the list with min value.

5	list(seq)
Converts a tuple into list.

Python includes following list methods

Sr.No.	Methods with Description
1	list.append(obj)
Appends object obj to list

2	list.count(obj)
Returns count of how many times obj occurs in list

3	list.extend(seq)
Appends the contents of seq to list

4	list.index(obj)
Returns the lowest index in list that obj appears

5	list.insert(index, obj)
Inserts object obj into list at offset index

6	list.pop(obj=list[-1])
Removes and returns last object or obj from list

7	list.remove(obj)
Removes object obj from list

8	list.reverse()
Reverses objects of list in place

9	list.sort([func])
Sorts objects of list, use compare func if given

# --------------------------------------------------------------------------

Python Expression	Results	Description
len([1, 2, 3])	3	Length
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	True	Membership
for x in [1, 2, 3]: print x,	1 2 3	Iteration

