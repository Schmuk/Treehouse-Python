import datetime

now = datetime.datetime.now()

# strftime - lets us turn a date, time, or datetime into a string
# formatted the way we want
# string from time

print(now.strftime('%B %d'))  # %B is the month
print(now.strftime(('%m/%d/%y')))

# strptime string parsed into time
birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d')

print('birthday = {}'.format(birthday))

birthday_party = datetime.datetime.strptime('2015 04 21 12:00', '%Y %m %d %H:%M')  # H 24 hr clock 1pm would be 13
# to not specify am and pm
print(birthday_party)