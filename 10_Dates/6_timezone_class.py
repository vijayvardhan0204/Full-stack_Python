'''CLASS: datetime.timezone
(For timezone handling)
👉 Methods / Attributes:
utc
offset using timedelta
tzname()'''

from datetime import datetime, timezone, timedelta

# UTC timezone
utc_time = datetime.now(timezone.utc)
print("UTC Time       =", utc_time)

# Custom Timezone (IST = UTC + 5:30)
ist = timezone(timedelta(hours=5, minutes=30))
ist_time = datetime.now(ist)
print("IST Time       =", ist_time)

# tzname()
print("tzname()       =", ist_time.tzname())
