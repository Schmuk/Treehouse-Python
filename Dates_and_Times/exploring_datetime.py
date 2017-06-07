import datetime

# do same thing
now = datetime.datetime.now()  # takes timezone
today = datetime.datetime.today()  # does not take timezone

# print(now)
# print(today)

today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today)
print(today.month)
print(today.hour)
print(today.year)

print(now.year)

print(today.weekday())  # weekdays are a list, Monday is 0

# print(now.timestamp())

my_delta = now - today
print('my_delta: {}'.format(my_delta))
print(datetime.timedelta.total_seconds(my_delta) / 60)

def minutes(dt_1, dt_2):  # timedelta minute challenge
    my_delta = dt_2 - dt_1
    my_seconds = datetime.timedelta.total_seconds(my_delta)
    return round(my_seconds / 60)

