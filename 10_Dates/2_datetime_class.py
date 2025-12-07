'''CLASS: datetime.datetime

(Contains date + time)

Common Methods:
now()
today()
utcnow()
strftime()
strptime()
replace()
fromtimestamp()
timestamp()
date()
time()'''
import datetime

# Current date & time
dt = datetime.datetime.now()
print("now()          =", dt)

# Today's date & time
print("today()        =", datetime.datetime.today())

# Current UTC time
print("utcnow()       =", datetime.datetime.now(datetime.UTC))

# Converting datetime → string
print("strftime()     =", dt.strftime("%Y-%m-%d %H:%M:%S"))

# Converting string → datetime
s = "2025-12-06 14:30:00"
parsed = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print("strptime()     =", parsed)

# Replace parts of datetime
new_dt = dt.replace(year=2030, month=1)
print("replace()      =", new_dt)

# Timestamp → datetime
# A timestamp is the number of seconds since 1 January 1970 (Unix Epoch).
print("fromtimestamp()=", datetime.datetime.fromtimestamp(1700000000))

# Datetime → timestamp
# Convert date → seconds number
print("timestamp()    =", dt.timestamp())

# Extract date only
print("date()         =", dt.date())

# Extract time only
print("time()         =", dt.time())
