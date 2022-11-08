# define a non-empty tuple
car = ('Ford', 'Escort',1300,'Red')
car_2 = 'Ford', 'Escort', 1300, 'Red'

# define an empty tuple
empty_tuple = ()
empty_tuple_2 = tuple()


print(car)
print(type(car))
print(car_2)

# access value by index

model = car[1]
print(model)

#  can't modify tuples

# car[1] = 'Focus' not allowed

colour = car[-1]
print(f'Model: {model} colour: {colour}')

# count tuple elements

tuplecount = len(car)
print(tuplecount)

fruits = ('apple', 'apple', 'banana','orange','nectarine','nectarine','nectarine')
print(fruits.count('nectarine'))

# tuple of a single element
single_tuple = ('ben',)
print(type(single_tuple))