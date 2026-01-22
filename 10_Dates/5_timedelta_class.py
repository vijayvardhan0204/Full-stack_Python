'''CLASS: datetime.timedelta
(Represents difference between dates / times)
Methods / Attributes:
days
seconds
microseconds
Supports +, -, *, / operations''

import datetime

# Difference of 5 days and 2 hours
td = datetime.timedelta(days=5, hours=2)
print("timedelta      =", td)

print("days           =", td.days)
print("seconds        =", td.seconds)
print("microseconds   =", td.microseconds)

# Current time + timedelta
now = datetime.datetime.now()
future = now + td
print("Future time    =", future)

# Subtracting dates
d1 = datetime.datetime(2025, 1, 1)
d2 = datetime.datetime(2025, 1, 10)
diff = d2 - d1
print("difference     =", diff)
