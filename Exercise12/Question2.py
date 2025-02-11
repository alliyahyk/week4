#   What is going on here? Can you explain the output?

tup = 'Hello'
print(len(tup))

#   output stream = 5
# tup           is a variable that stores the string 'Hello'.
# len(...)      is a function that returns the number of elements in an object.
#               In this case, returns the length of the associated string, which is 5.


tup = 'Hello',
print(len(tup))

#   output stream = 1
# , (comma)     The comma turns the string into a tuple with one element.
#       Reason: A Tuple is defined by commas, not parentheses.
#               The length of a tuple is determined by the number of elements it contains,
#               not the length of the element itself.

