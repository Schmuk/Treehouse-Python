'''Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] '''

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

def change_last_value(input_data):
    fixed_list = []
    for item in input_data:
        new_item = item[::len(item) - 1] + (100,)
        fixed_list.append(new_item)
    return fixed_list

print(change_last_value(sample_list))