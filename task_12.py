import random
# Exercise 12: Q1
cheese_example = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese_example += 'oke'
print(cheese_example)
# the problem is the output is oke separated with commas

# .append() method could have been used like below to include oke
cheese_liya = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese_liya.append('Oke')
print(cheese_liya)
# append method does not allow two arguments however

# adding two arguments in a single command using .extend() method
# you can use the .extend() method on line 16 to continue adding more cheeses as this method takes iterables like lists
cheese_liya_twoarg = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese_liya_twoarg.extend(['Oke', 'Mozzarella'])
print(cheese_liya_twoarg)

# Exercise 12: Q2
# This is printing the length of letters in the tup variable which is 'Hello'
tup = 'Hello'
print(len(tup))

# This is printing the amount of strings in the variable
# with just 'Hello' the output would be 1 but i have included 3 below
# 3 strings using len on the tup2 variable makes the output 3
tup2 = 'Hello', 'example', 'example2',
print(len(tup2))

