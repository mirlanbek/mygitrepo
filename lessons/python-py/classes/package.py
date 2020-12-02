import os , sys
import pack_support as ps

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), ".."))

test = ps.Project_Map()
my_file = ps.Project_Map().root_path() + "/miki.conf"


print(  test.root_path()  )

print(  ps.Project_Map("Beka").r    )
print(my_file)




