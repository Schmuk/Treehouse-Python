# Write a Python program to count the elements in a list until an element is a tuple.

my_list = ['Hello There', 3, 139, 'Dank Memes', ('stop', 'here'), 'abc', 'asdf', 99] # 8 elements
another_list = ['Another One', 3, 555, ('a', 'b')]
def count_until_tuple(a_list):
    count = 0
    for item in a_list:
        if isinstance(item, tuple):
            break
        else:
            count += 1
    return count

print(count_until_tuple(my_list))
print(count_until_tuple(another_list))

'''
counts until the tuple is hit.  The count includes the tuple so the returned value is 5.
uncomment to count the elements before the tuple is hit.  Does not include the tuple so returned value is 4



'''