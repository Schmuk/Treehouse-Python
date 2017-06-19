# Write a function named first_number that takes a string as an argument. The function should search, with a regular expression, the first number in the string and return the match object.


import re

def first_number(arg):
    match = re.search(r'\d', arg)
    return match
  
  
def numbers(count, arg):
    return re.search(r'\d' * count, arg)