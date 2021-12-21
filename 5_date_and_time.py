import datetime
dt = datetime.datetime.now()
print(dt)
print(datetime.MINYEAR, datetime.MAXYEAR)
print(datetime.time)
print(datetime.datetime.now())
print(datetime.datetime)
print(datetime.timedelta)
print(datetime.tzinfo)
print(datetime.timezone)
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=8457757,
    milliseconds=588549835,
    minutes=8768,
    hours=847,
    weeks=48

)
print(delta)
# print(timedelta.total_seconds(days=365))    --->show error
year = timedelta(days=365)
print(year.total_seconds())

# date object
from datetime import date
print(date.today())
print(date.fromisoformat('2019-12-04'))
print(date.min)
print(date.max)
print(date.year)
print(date.month)
print(date.day)
print(date.today()+timedelta(days=2))