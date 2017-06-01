
def my_packer(name = None, **kwargs):
    print(kwargs)
    print(name)

my_packer('Conor', age = 22, favorite_game = 'Overwatch')

def unpacker(first_name = None, last_name = None, age = 0):
    if first_name and last_name:
        print('hi {} {}'.format(first_name, last_name))
    else:
        print('Hi no name')
    print(age)

unpacker(**{'first_name': 'Conor', 'last_name': 'Fitzgerald', 'age': 22})