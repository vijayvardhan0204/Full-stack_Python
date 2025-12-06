'''CLASS: datetime.date
(Contains only date)
Methods:
today()
fromtimestamp()
isoformat()
replace()
weekday()
isoweekday()'''

import datetime

d = datetime.date.today()
print("today()        =", d)

# Create custom date
d2 = datetime.date(2025, 12, 25)
print("custom date    =", d2)

# Timestamp → date
print("fromtimestamp()=", datetime.date.fromtimestamp(1700000000))

# ISO format
print("isoformat()    =", d.isoformat())

# Replace fields
print("replace()      =", d.replace(year=2030))

# Monday = 0 ... Sunday = 6
print("weekday()      =", d.weekday())

# Monday = 1 ... Sunday = 7
print("isoweekday()   =", d.isoweekday())
