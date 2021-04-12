import os,sys,time,datetime

---------------------
start_time = time.time()
time.sleep(5)
diff = time.time() - start_time

print(diff)    =====>  5 chygat sebebi 5 second es algan raznica
----------------------

d=datetime.date(2017,10,23)
print(d)

d2 = datetime.date.today() 
print( d2   )

print(  d2.day, d2.weekday(),       )

t = datetime.time(9,18,6)

print(t.hour)

==========================================================
from datetime import datetime, date, timedelta
import random

for i in range(0,7):
    print (date.today - timedelta(days=i))
=============================================================


start_time = datetime(year=2019, month=4, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')

print(d2) 

today = date(2014, 10, 3) # or you can do today = date.today() for today's date



    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)  # NOTE: proccess value '1985' and get '34' then return it as cls arg


