number_list = [1, 2, 3]

# add items to list
number_list += [4, 5, 6]

number_list.append(7) # add single item to list

number_list.extend([8, 9, 10, 10, 10, 10]) # add multiple items to list

number_list.remove(1)

my_number = number_list.pop(3)

print(number_list)
print('my number is: {}'.format(my_number))
print('there are {} 10s in my list'.format(number_list.count(10)))

def add_two_to_list_items(list_of_nums):
    new_list_of_nums = []
    for number in list_of_nums:
        new_list_of_nums.append(number + 2)
    return new_list_of_nums

print(add_two_to_list_items(number_list))

restricted_list = number_list[3:6] # [6, 7, 8]
print(restricted_list)

reverse_list = number_list[::-1]
print(reverse_list)