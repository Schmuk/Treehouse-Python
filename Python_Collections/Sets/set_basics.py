
# set creation

old_way = set([1, 2, 3])
# print(type(old_way))
# print(old_way)

new_way = {1, 3, 5, 7, 9}
# print(type(new_way))
# print(new_way)

empty_set = set()
# print(type(empty_set))
# print(empty_set)

no_order = {9, 1, 100, 250, 333}
# print(no_order)

low_primes = {1, 3, 5, 7, 9, 11, 13}
low_primes.add(17) # use add() to add single item to set
#print(low_primes)

low_primes.update({19, 23, 27}) # update() for multiple items
# print(low_primes)

low_primes.update({2, 4, 6, 8, 10, 12}, {14, 16, 18, 20},
                  {22, 24, 26}) # sets can be updated with multiple sets

# print(low_primes)

low_primes.remove(27) # remove item from set
# print(low_primes)

low_primes.discard(27) # search set for item, if its not there it just goes on

low_primes.pop() # removes item at front of set
# print(low_primes)