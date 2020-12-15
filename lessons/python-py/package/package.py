import os , sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "pack_support"))

import pack_support as ps
import friends

print(friends.Friends())

test = ps.Project_Map("miki.conf")
my_file = test.root_path()

print(my_file)






