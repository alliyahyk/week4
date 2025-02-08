# Exercise 3: lotto.py
# lotto is a variable which is using random module that has been imported
# .sample() is a method that returns a list with random numbers in the range set between 1 and 50
# 6 is the number of random numbers it should collect
lotto = random.sample(range (1,50),6)
print(lotto)

# best data storage types
# a tuple is immutable so the value cannot be changed after it is created
tuple_lotto = tuple(lotto)
print(tuple_lotto)

# alternatively frozen set could freeze the numbers and make them unchangeable
freeze = frozenset(lotto)
print(freeze)
