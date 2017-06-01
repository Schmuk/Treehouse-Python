myself = {'name' : 'Conor', 'age' : 22, 'favorite games' : ['Overwatch', 'ESO', 'Pokemon'],
          'favorite songs' : {'Linkin Park' : 'Iridescent', 'Breaking Benjamin': 'Ashes of Eden', 'Skillet' : 'Stars'}}

'''
print(myself)
print()
print(myself.values()) # prints the values in the dictionary
print()
print(myself.items()) # prints the keys and values
print()
print(myself.keys()) # prints the keys in the dictionary
'''
myself.update({'favorite animal' : 'dog'})
print()
print(myself)

'''
# Accessing and updating a dictionary value
myself['favorite songs']['Skillet'] = ['Stars', 'Forgiven'] # use update for multiple items
myself['role'] = 'sniper' # add new key, value pair
'''