
#------------- break bested loops with "return"------------------

def break_all_loops():
   while True:
      for i in range(20):
         if i == 7:
             return

# -------------- get reverse of str ---------------

a="mirlan" 
print(a[::-1])  # ----------- 'nalrim' chygat

# 2)
rev=''.join(reversed(a))
print(rev)       # ----------- 'nalrim' chygat

           
# -------------------- list existng methods in class-----


p1 = Class()

dir(p1)

help(p1)

print(hasattr(p1, "age"))

# ---------- fibbonochi ----------
a, b = 0,1

for i in range(10):
    print(b)
    a,b = b, a+b

# ---------- FizzBuzz----------------------


for i in range(100):
    if (i % 3) == 0 and (i % 5) == 0:     # Note % is gives reminder (kaldyk) M: 10 % 3 = 1,  11 % 3 = 2, 12%3=0, 13%3=1
        print(i)
        print("fizzBuzz")
    elif i % 3 == 0:
        print(str(i) + " fizz")
    elif i % 5 == 0:
        print(str(i)+" buzz")

# ---------------------- Unpacking -------------

a,b,*c = (1,3,4,5,6)

print(a)
print(b)
print(c)
||
\/
1
3
[4,5,6]   means c=rest of list

a,b,*_ = (1,3,4,5,6)

now we can use only a and b  ignore rest

# -------------- zip(list1,list2)--------------------
list1 = [1,2,3,4,5]
list2 = ["bir", "eki", "uch", "tort", "besh"] 

for num,name in zip(list1, list2):
    print('anyn nomeri {}, jana aty {}'.format(num, name)  )

# ----------------------------------

sum = 100_000 + 20_001    # undescore doesnt change result
print(sum)      #--- is works as expected

also:  print ( f'{num:,}' )   # divde output with ',':  120,000

-------------------- README to html --------------------------------------------------------

import markdown
with open('README.md', 'r') as markdown_file:

    # Read the content of the file
    content = markdown_file.read()

    # Convert to HTML
    print(markdown.markdown(content))



--------------os.flush()-------os.fsync()--------------------------------
import os 
path = 'file.txt'
fd = os.open(path, os.O_RDWR) 

os.write(fd, str) 

f.flush() 
# The written string is 
# available in program buffer 
# but it might not actually  
# written to disk until 
# program is closed or  
# file descriptor is closed.  
  
# sync. all internal buffers 
# associated with the file descriptor 
# with disk (force write of file) 
# using os.fsync() method 
os.fsync(fd) 
print("Force write of file committed successfully") 
  
# Close the file descriptor  
os.close(fd) 
Output:

Force write of file committed successfully
-----------------------------------------------------



                    time.sleep(20)
                    os.kill(os.getpid(), 9)

-----------------------------------------------------------
#  isinstance(obj, class)
# check if 'obj' belongs to class 'class'

test_int = 5
test_str = "GeeksforGeeks"
test_list = [1, 2, 3]

# testing with isinstance
print ("Is test_int integer? : " + str(isinstance(test_int, int)))
print ("Is test_int string? : " + str(isinstance(test_int, str)))
print ("Is test_str string? : " + str(isinstance(test_str, str)))
print ("Is test_list integer? : " + str(isinstance(test_list, int)))
print ("Is test_list list? : " + str(isinstance(test_list, list))


------------------------------------------------------
import collections

i="Mirlan  :   Tokonbekov"

my_dict = collections.OrderedDict()

d_key, d_value = i.split(" : ", 2)  # type: str
my_dict[d_key.strip()] = d_value.strip()

print(my_dict)

