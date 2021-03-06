# https://www.youtube.com/watch?v=UK97NoQK23k

doc1 = """
 
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



doc2 = """

mkdir pachage

create  package/__init__.py  ==>  from .friends import meth                          (VERY IMP)
        package/friends.py ==>  def meth(): print ('i'm from package/friends.py')

to access:

vi start.py:

	from package import *
	meth() 


"""

doc3 = """

--------------- Access form 1 module to another one inside package:

mkdir pachage

create  package/__init__.py  ==>  from .friends import meth                          )
        package/friends.py ==>  def meth(): print ('i'm from package/friends.py')
        package/dos.py ==>  Class ClassName(): print ('i'm from package/dos.py')

to access:

vi dos.py:

        from friends import ClassName
        a = ClassName()


"""

doc4 = """



--------------- Access import class form package.py to sub_package.py:  

vim sub_package.py =>
from ../package import * 

mkdir pachage

create  package/__init__.py  ==>  from .friends import meth                          )
        package/friends.py ==>  def meth(): print ('i'm from package/friends.py')
        package/dos.py ==>  Class ClassName(): print ('i'm from package/dos.py')

	package/sub_package/__init__.py 
	package/sub_package/sub_package.py
 
to access:

vi sub_package.py:

        from ..friends import ClassName
        a = ClassName()


"""
doc5 = """

# conclusion for package accessing 

main.py                         --------------->:   from package impot ClassName   ;  a=ClassName()   ; print(a.var)  ==> "Salam"  chygat    

package/__init__.py             --------------->:   from .sub_package import *      je ClassName
package/sub_package/__init__.py --------------->:   from .module import *           je ClassName
package/sub_package/module.py   --------------->:   class ClassName(): var="salam"

"""

doc6 = """
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
    
    -------- in subpackageN/__init__.py --can be accessed like following: -------------------- ------------------------- 
    
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
    

"""

