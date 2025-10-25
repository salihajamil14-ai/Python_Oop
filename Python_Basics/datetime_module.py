# Datetime Module Basics

# Importing the datetime module
import datetime

# Importing the pytz module for working with time zones
import pytz

# Getting the current date and time
d = datetime.date(2023, 3, 14)
print(d)  # 2023-03-14s

tday = datetime.date.today()
print(tday)  # 2023-03-14

# Accessing individual components of the date
tday = datetime.date.today()
print(tday.day)  # 14
print(tday.month)  # 3
print(tday.year)  # 2023   
print(tday.weekday())  # 1 (Monday is 0)
print(tday.isoweekday())  # 2 (Monday is 1)

# Date arithmetic using timedelta
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)  # 2023-03-21
print(tday - tdelta)  # 2023-03-07

# Calculating the difference between two dates
bday = datetime.date(2024, 6, 18)
till_bday = bday - tday
print(till_bday.total_seconds())  # Number of seconds until birthday

# Working with time objects
t = datetime.time(9, 30, 45, 100000)
print(t)  # 09:30:45.100000
print(t.hour)  # 9

# Working with datetime objects
dt = datetime.datetime(2023, 3, 14, 9, 30, 45, 100000)
print(dt)  # 2023-03-14 09:30:45.100000
print(dt.date())  # 2023-03-14
print(dt.time())  # 09:30:45.100000
print(dt.year)  # 2023

# Datetime arithmetic
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)  # 2023-03-14 21:30:45.100000
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)  # Current local date and time
print(dt_now)    # Current local date and time
print(dt_utcnow) # Current UTC date and time

# Pytz for timezone handling
dt = datetime.datetime(2023, 3, 14, 9, 30, 45, tzinfo=pytz.UTC)
print(dt)  # 2023-03-14 09:30:45+00:00

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)  # Current UTC date and time with timezone info

dr_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)  # Current UTC date and time with timezone info

dt_mtn = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
print(dt_mtn)  # UTC time converted to US/Mountain timezone 

# Listing all available time zones
for tz in pytz.all_timezones:
    print(tz)  # Prints all available time zones
    
# Current date and time in US/Eastern timezone
dt_eastern = datetime.datetime.now(tz=pytz.timezone("US/Eastern"))
print(dt_eastern)  # Current date and time in US/Eastern timezone

dt_mtn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))
print(dt_mtn.strftime("%B %d, %Y"))  # Formatted date in US/Mountain timezone
dt_str = 'july 26, 2024'

dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)  # 2024-07-26 00:00:00