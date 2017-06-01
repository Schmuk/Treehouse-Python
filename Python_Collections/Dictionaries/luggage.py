def packer(**kwargs):
    print(kwargs)


# name is not included in the kwargs dictionary, name caught outside of the packing
'''def packer(name = None, **kwargs):
    print(kwargs)'''

def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print('Hello there {} {}'.format(first_name, last_name))
    else:
        print('Hello no name')

packer(name = 'Conor', num = 25, spanish_inquisition = None)
unpacker(**{'last_name' : 'Fitzgerald', 'first_name': 'Conor'})
# unpacks dictionary and passes values to function



'''
In Python when you use ** on a parameter in a function Python will pack those keyword
arguments into a dictionary
'''

'''*****kwargs is a dictionary*****'''

course_minutes = {'Python Basics' : 232, 'Django Basics' : 237, 'Flask Basics' : 189,
                   'Java Basics' : 133}


for course, minutes in course_minutes.items():
    print('{} is {} minutes long'.format(course, minutes))