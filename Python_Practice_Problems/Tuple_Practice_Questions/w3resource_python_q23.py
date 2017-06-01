''' Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] '''


sample_data = [('item_1', '12.20'), ('item_2', '15.10'), ('item_3', '24.5')]

sorted_list_by_float = []

for item in sample_data:
    sorted_list_by_float.append(item)

    if item[1] > sorted_list_by_float[0][1]:
        sorted_list_by_float.insert(0, item)
        sorted_list_by_float.pop()

# print(sorted_list_by_float)

def sort_with_tuple_float_value(input_data):
    sorted_list = []
    for item in input_data:
        sorted_list.append(item)

        if item[1] > sorted_list[0][1]:
            sorted_list.insert(0, item)
            sorted_list.pop()
    return sorted_list

print(sort_with_tuple_float_value(sample_data))


