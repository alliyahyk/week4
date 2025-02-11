#   What is wrong with this?

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# print(cheese)

# Output stream: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']

# cheese = ['','','']       is a list of string literals (3 arguments) stored in variable, 'cheese'.

# cheese += 'Oke'           The += operator extends the list with elements of the iterable (a sequence of characters) on the RHS.
#                           Problem: 'Oke' is a string. When you use += with a list and a string, the string is treated as an iterable.
#                           Each character in 'Oke' are added to the list as separate elements.


#   Solution: Adding 'Oke' as a single element
cheese += ['Oke']

# Incorporating [...] enables 'Oke' to be added to the list as a single element.
# We are wrapping it in a list rather than splitting characters.

#   How would you add two new cheese to the list with a single command?

cheese.extend(['Camembert', 'Parmesan'])
print(cheese)

#   or
# cheese += ['Brie', 'Mozzarella']