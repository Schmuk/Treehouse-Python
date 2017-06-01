first_number = 5
second_number = 20
third_number = 2.2
forth_number = 3.3

# addition
my_sum = first_number + second_number
print('the sum of my numbers is:', my_sum)

# subtraction
my_difference = second_number - first_number
print('the difference of my numbers is:', my_difference)

# multiplication
my_product = first_number * second_number
print('the product of my numbers is:', my_product)

# division

my_quotient = second_number / first_number
print('my quotient is %d' % my_quotient) # print formatting, division always returns floats
print(type(my_quotient))

print()

print('float addition:', third_number + first_number)
print('float subtraction:', third_number - first_number)
print('float multiplication:', third_number * first_number)
print('float division:', third_number / first_number)

print()
print('Weird things about floats')
print(0.1 + 0.1 + 0.1 - 0.3)

print('round function, rounds float to nearest whole number'
      ' which in this case is:', round(5.551115123125783e-17))
'''
use the int() function to convert a float to an int.  Returns the int value 
(chops of float portion), i.e. 5.2 becomes 5, 5.9 becomes fine.
'''

order_of_ops = (5 + 5) / 2 + 5

