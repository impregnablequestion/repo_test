# create empty lists
empty_1 = []
empty_2 = list()

# create a list with some items
fruits = ['apple', 'banana', 'orange']

fruits[1] = 'papaya'

# get the number of items
# print(len(fruits))

# add a new fruit
# fruits.append('yuzu')

# remove fruit from list

# added fruit
removed_fruit = fruits.pop(0)
print(f'I removed {removed_fruit}')
print(f'My fruits are now {fruits}')