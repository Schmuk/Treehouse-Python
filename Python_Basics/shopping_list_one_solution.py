shopping_list = []

print('What should we pick up at the store?')
print("Enter 'DONE' to stop adding items.")

while True:
    new_item = input('> ')

    shopping_list.append(new_item)

    if new_item == 'DONE':
        shopping_list.remove('DONE')
        break

print('Here is you list')

for item in shopping_list:
    print(item)