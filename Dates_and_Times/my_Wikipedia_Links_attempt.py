import datetime
import urllib.request

print('Enter a date to date with the in the following format')
print('month name, day number')
query_date_string = input('> ')

while True:

    if query_date_string == 'DONE'.lower():
        break


    query = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + query_date_string)

    print(query.geturl())

    query_date_string = input('Enter another date or DONE to quit ')






