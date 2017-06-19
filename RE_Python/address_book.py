import re

names_file = open("names.txt", encoding="utf-8")  # creates a pointer to a file
data = names_file.read()
names_file.close()  #  releases memory

last_name = 'Love'
#print(re.match(last_name, data))  # beginning of string
#print(re.search(r'Kenneth', data))  # somewhere in string
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))  # entire string, multiple occurances
#print(re.findall(r'\w*, \w+', data))
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))

#print(re.findall(r'''
#    \b@[-\w\d.]*  # Find a word boundary, an @, and #any number of characters
#    [^gov\t]+  #  Ignore 1+ instances of the the letters 'g', 'o', or 'v' and a tab
#    \b
#''', data, re.VERBOSE | re.I))  #  pipe symbol b/t flags to have multiple flags
#print(re.findall(r'''
#\b[-\w]*,  # Find a word boundary, 1+ hyphens or characters, and a comma
#\s  # Find 1 whitespace
#[-\w ]+  # 1+ hyphens and characters and explicit spaces
#[^\t\n]  # ignore tabs and newlines
#''', data, re.X))  #  short hand of re.VERBOSE
line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # groups defined with (), last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # emails
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # job and company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', data, re.X | re.MULTILINE)

print(line)
print(line.groupdict())