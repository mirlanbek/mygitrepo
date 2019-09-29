
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

