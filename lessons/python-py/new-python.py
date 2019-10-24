
# ---------------------- seattr -------------

class Person():
    pass

p = Person()

key = 'name'
val = 'Miki'

setattr(p, key, val)

print(p.name)

****
output: Miki
-----------------
name = getattr(p, key)
print(name)
-----------------------------------------------
person = Person()
person_info = { 'first': 'Miki', 'last': 'Tokon' }
for key,value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))



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

