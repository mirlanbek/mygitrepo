
# Generator is "yield", and it is used like "return" in a function only, but returns when you call with "next()"
# for i in 1000000000000: here generator helps loop by one and stop, otherwise memory cannot handle big number  


# my_nums = iter([1,2,3,4])

# for i in my_nums:
#     print (i)


def sq_nums(nums):
    
    for i in nums:
        yield i*i


p1 = sq_nums([1,2])

print(next(p1))
print(next(p1))

print(next(my_nums))
print(next(my_nums))

def sq_nums(nums):
    
    for i in nums:
        yield i*i


p1 = sq_nums([1,2])

print(next(p1))
print(next(p1))



my_nums = (k for k in [1,2,3,4])

print(next(my_nums))

for t in my_nums:
    print(type(my_nums))
    print(t)

#################################

def sq_nums(nums):
    
    for i in nums:
        yield i*i


p1 = sq_nums([1,2])

print(next(p1))
print(next(p1))

my_nums = (k for k in [1,2,3,4])

# print(next(my_nums))

for t in my_nums:
    print(type(my_nums))
    print(t)    


def gerator(list):
    for i in list:
        yield i

list = ["bir", "eki", "uch", "tort", "besh"]

a = gerator(list)

o = len(list)
while  o > 0:
    print(  next(a)  )
    o -= 1

# +++++++++++++++++++++++++++++++++++++

def gener(st):
    yield st

a = gener("Miki")

print (next(a))

