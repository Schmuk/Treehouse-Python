my_input = ["apple", 5.2, "dog", 8]

def combiner(value_list):
    combined = ''
    sum = 0
    for value in value_list:
        if isinstance(value, str):
            combined = combined + value
        elif isinstance(value, (int, float)):
            sum = sum + value
    return combined + str(sum)

print(combiner(my_input))