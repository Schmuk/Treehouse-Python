# commas make the tuple, need a , after tuple members. ex tuple w/ 1 member 5,
my_name = ('Conor', 'Fitzgerald')
template = 'Hello my name is {} {}'

# print(template.format(*my_name))

for idx, my_name in enumerate(my_name):  # enumerate() returns index and corresponding value
    print('Hello')
