set1 = set(range(10))

set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

set_intersection = set1.intersection(set2)
# print(set_intersection)

set1_difference = set1.difference(set2) # values set1 has that set2 doesn't have
# print(set1_difference)

set2_difference = set2 - set1 # values that set2 has that set1 doesn't
# print(set2_difference)

set_symmetric_difference = set1 ^ set2 # the values that are different in both sets
# print(set_symmetric_difference)

set_union = set1 | set2 # combination of sets
# print(set_union)


### order matters when using difference function