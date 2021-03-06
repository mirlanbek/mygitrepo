from .countries import *
from .continent import *

from .europe import *
from . africa import *







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
    
-------------------------------------- ------------------------- 
    
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
    

"""
