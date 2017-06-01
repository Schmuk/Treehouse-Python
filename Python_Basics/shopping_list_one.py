import os

to_do_list = []
user_input = None
list_item = None
item_count = 1

print('''To add an item to your to do list enter \'ADD\'
To remove an item form your to do list enter \'REMOVE\'
To remove an item form your to do list enter \'REMOVE\'
To quit enter \'DONE\'
To view your list type \'SHOW\'
For help enter \'HELP\'''')



def help():
    print('''To add an item to your to do list enter \'ADD\'.
    To remove an item form your to do list enter \'REMOVE\'.
    To remove an item form your to do list enter \'REMOVE\'.
    To quit enter \'DONE\'.
    To view your list type \'SHOW\'.
    For help enter \'HELP\'.''')

def show_list(my_list):
    print('***** Your List *****')
    for thing in my_list:
        print(str(my_list.index(thing) + 1) + '. ' + thing)



while True:

    user_input = input('> ')

    if user_input == 'DONE':
        break

    elif user_input == 'ADD':
        list_item = input('Enter an item to add to your list ')
        to_do_list.append(list_item)

    elif user_input == 'REMOVE':
        list_item = input('Enter an item to remove from your list ')
        to_do_list.remove(list_item)

    elif user_input == 'HELP':
        help()
        continue

    elif user_input == 'SHOW':
        show_list(to_do_list)
        continue



show_list(to_do_list)




