
# ------------------------ lambda ------------------------------

#Anonimous function or Lambda

a = (lambda: "Salam Lambda")
print(a())




b = (     lambda x,y: x**y           )
print(b(2,3))


# ------------------------ map ------------------------------
# map degen listti ochered menen fanctiongo pass kylat, birok [ list bolup chygat ]


lis = [1,3,5]
def a (x):
    return x**2

w=map(a, lis)   # Note: a is func name, lis - list


for i in list(w):         # IMP: ALWAYS convert  "w"   to list(w) and for loop  to print them all   
    print(i)

----------- MAP is working on python 3+ ------

l=[1,2,3,4]

def test(s):
    return s * 2

for i in list(map(test, l)):   # convert to list, then for loop
    print(i)

# ******************  it also maps item pair, M: first name list with last name list *******************************************************


f= ['Mirlan', 'Melis', 'Doku']
l=['Alipsatarov', 'Kalyev', 'Bakirov', "Zakirova"]

def myfunc(f, l):
  return f + " " + l

x = map(myfunc, f, l)

for i in list(x):
    print(i)


# -------- reduce---------------------------------

# reduce is same as map, it  uses first result and accumlates to result

from functools import reduce
lis = [1,3,5, 6]
def a (x,y):
    return x * y   # 1*3=3 3*5=15 15*6=90 :)

w=reduce(a, lis)
print(w)



result: 90
if x+y: 15 chygat


