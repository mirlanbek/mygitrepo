_readme = """
 
Package == any folder with __init__.py in it

mkdir pachage

touch   package/__init__.py  (empty file ) it just turns folder to package
        package/friends.py ==>  def meth(): print ('i'm from package/friends.py')
        
to access: 
          import package.friends as fr
          fr.meth()

SUB-package:

mkdir pachage/subpackage

touch   package/subpackage/__init__.py  (empty file ) it just turns folder to package
        package/subpackage/dos.py ==>  def meth(): print ('i'm from package/subpackage/dos.py')
        
to access: 
          import package.subpackage.dos as dos
          dos.meth()
"""

import os , sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "pack_support"))

import pack_support as ps
test = ps.Project_Map("miki.conf")
my_file = test.root_path()

print(my_file)



from friends.osh import Univer as uni
uni().tcp()


print(_readme)