'''CLASS: datetime.time
(Contains only time)
Methods / Attributes:
hour
minute
second
microsecond
isoformat()
replace()'''

import datetime

t = datetime.time(10, 30, 45, 123456)
print("time           =", t)

print("hour           =", t.hour)
print("minute         =", t.minute)
print("second         =", t.second)
print("microsecond    =", t.microsecond)

print("isoformat()    =", t.isoformat())

# Replace time fields
print("replace()      =", t.replace(hour=5, minute=0))
