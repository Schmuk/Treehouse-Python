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

#def minutes(dt1, dt2):
 #   seconds = (dt2 - dt1).total_seconds()
  #  return round(seconds / 60)

# def time_tango(the_date, the_time):
    # new_datetime = datetime.datetime(year = the_date.year, month = the_date.month, day = the_date.day,
                                     # hour = the_time.hour, minute = the_time.minute, second = the_time.second,
                                     # microsecond = the_time.microsecond)
    # return new_datetime

# def time_machine(integer, string):
  # if string == 'hours':
    # return starter + datetime.timedelta(hours = integer)
  # elif string == 'days':
    # return starter + datetime.timedelta(days = integer)
  # elif string == 'years':
        # the_years = starter.days * 365
    # return starter + datetime.timedelta(days = the_years)
  # elif string == 'minutes':
    # return starter + datetime.timedelta(minutes = integer)

def timestamp_oldest(*args):
  return datetime.datetime.fromtimestamp(min(args))
#  smallest time is the oldest, later/newer times would be bigger
#  measurement taken at 5 seconds is older than one taken at 15 seconds