phrase = 'Rise and rise again until lambs become lions'
another_phrase = "Just because someone stumbles and loses their way"

my_sentence = "methods to deal with 's in words, he's right"
method_2 = 'he\'s right' # escape apostrophe in the string
method_3 = '''He's right''' + '''and he's a meme''' # triple quotes


print(my_sentence)
print(method_2)

name = 'Conor'
name += ' Fitzgerald'
print(name)

# you can multiply string

print('a' * 5)

# format method
my_word = 'ugly'
funny_phrase = 'I\'m {} and I\'m proud!'.format(my_word)
print(funny_phrase)

# strings are a collection of characters

greetings = 'Hello there sir asshole!'

word_list = greetings.split() # splits on spaces by default

flavors = ['Cookies and cream', 'Mint chocolate chip', 'coffee']

flavors_string = ', '.join(flavors)
print(flavors_string)

print('My favorite flavors are: {}'.format(' ,'.join(flavors)))

the_sea = greetings[12] + greetings[1] + greetings[16]
print(the_sea)