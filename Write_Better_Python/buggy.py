# import pdb

my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

# pdb.set_trace()
# import pdb; pdb.set_trace()
del my_list[3]  # [5, 2, 1, "abcdefg", 3, False, 4]
del my_list[3]  # [5, 2, 1, 3, False, 4]
del my_list[4]  # [5, 2, 1, 3, 4]
print(my_list)


# > /home/treehouse/workspace/buggy.py(9)<module>() The line we are on
# -> print(my_list) next line to br run
# (Pdb) n