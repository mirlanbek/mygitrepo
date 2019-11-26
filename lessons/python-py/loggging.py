# DEBUG: Detailed information, for diagnosing problems. Value=10.
# INFO: Confirm things are working as expected. Value=20.
# WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
# ERROR: More serious problem, the software is not able to perform some function. Value=40
# CRITICAL: A serious error, the program itself may be unable to continue running. Value=50

# --------------------------  My test --------------------------
import logging

# logging.basicConfig(filename="test.log", level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test.log")
formatter=logging.Formatter('%(asctime)s  :: %(name)s :: %(levelname)s :: %(message)s')
file_handler.setFormatter(formatter)

loger.addHandler(file_handler)

def test(**kargs):
    for key,val in kargs.items():
        msg = "key: {}, val: {}".format(key,val)
        print(msg)
        loger.info(msg)

test(name="Doku", lastname="Bakirov")

# -----------------------------------------------------------


import logging
logging.basicConfig(level=logging.WARNING)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5

kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}

logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))
logging.error("a={a} and b={b} cannot be negative".format(**kwargs))
logging.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))

# output:

# WARNING:root:a=3 and b=4 are equal
# ERROR:root:a=3 and b=4 cannot be negative
# CRITICAL:root:Hypotenuse of 3, 4 is 5.0


# -------------- Format -------------------------------------------------------------


logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
logging.info("Just like that!")
#> 2019-02-17 11:40:38,254 :: INFO :: Just like that!


# ----------------------- New logger -----------------

logger = logging.getLogger(__name__)
logger.info('my logging message')
        
# Now, once you ve created a new logger, you should remember to log all your messages using 
# the new logger.info() instead of the roots logging.info() method.

# ---------------------------------------------------------------------

# What is and How to set up a File Handler and Formatter?
# The FileHandler() and Formatter() classes are used to setup the output file and the format of messages for loggers other than the root logger.

# Do you remember how we setup the filename and the format of the message in the root logger (inside logging.basicConfig()) earlier?

# We just specified the filename and format parameters in logging.basicConfig() and all subsequent logs went to that file.

# However, when you create a separate logger, you need to set them up individually using the logging.FileHandler() and logging.Formatter() objects.

# A FileHandler is used to make your custom logger to log in to a different file. Likewise, a Formatter is used to change the format of your logged messages.


# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')


# OUTPUT:

# 2019-09-20 09:39:54,398 :: INFO :: Just like that!
# 2019-09-20 09:39:54,398 :: INFO :: my logging message
# 2019-09-20 09:39:54,399 :: WARNING :: Something is not right.
# 2019-09-20 09:39:54,399 :: ERROR :: A Major error has happened.
# 2019-09-20 09:39:54,399 :: CRITICAL :: Fatal error. Cannot continue

