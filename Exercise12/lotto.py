import random

# random                    is a module that provides functions for generating random numbers.
#                           selecting random items and performing operations revolving around randomness.

# random.randint(a,b)       Returns a random integer N within the range a ≤ N ≤ b, where a is lower bound, and b is upper bound.

# random.sample(population, k)
#                           Returns a random sample of unique elements k from a population (list, tuple, set, or range).
#                           Does not repeat any element in the sample.

# random.random()           Returns a random floating number between 0.0-1.0.

# random.choice(sequence)   Returns a random element from a sequence (list, tuple).

# random.shuffle(sequence)  Shuffles the elements of a sequence.

# set()

#   Example 1: using FOR LOOP
lottery_numbers = []

for lottery in range(6):
    num = random.randint(1, 50)
    lottery_numbers.append(num)
print(f"Your lottery numbers are:{lottery_numbers}\nGood luck!")

# Numbers are stored in a list because lists are ordered (ordering of numbers matter in a lottery)
#   and mutable (elements can be easily modified with methods like .append())
# For loop      enables iteration 6 times to generate 6 numbers via range(6) which produces the sequence, 0,1,2,3,4,5.
# lottery       is a loop variable
# num           if num is between range 1<num<50, then that number is added to the list.
# append()      adds elements to the end of a list.


#   Example 2: using FOR LOOP, alternate structure
lottery_numbers = [random.randint(1, 50) for lottery in range(6)]
print(f"Your lottery numbers are:{lottery_numbers}\nGood luck!")


#   Example 3: using list
lottery_numbers = list(range(1,50))
random.shuffle(lottery_numbers)
lottery_numbers = lottery_numbers[:6]
print(f"Your lottery numbers are:{lottery_numbers}\nGood luck!")

# list(range(...)   create a list of integers from 1-50
# random.shuffle()  randomly reorders the integers of the list.
# [:6]              is a slice operator that extracts the first 6 elements of the list after shuffling.
#       alternative: can use for loop with range(6) and use .pop()

#   Example 4: using random.sample()
lottery_numbers = random.sample(range(1,50),6)
print(f"Your lottery numbers are:{lottery_numbers}\nGood luck!")
# From a population of integers within range 1-50, return 6 random integers.


#   Example 5: using WHILE LOOP
lottery_numbers = []

while len(lottery_numbers) != 6:
    num = random.randint(1,50)
    lottery_numbers.append(num)
print(f"Your lottery numbers are:{lottery_numbers}\nGood luck!")

# len(...) =! 6  sets list to 6 numbers.

#   lOTTO SET

lotto_set = set()

while len(lotto_set) < 6:
    lotto_set.add(random.randint(1,50))

print(lotto_set)

# reorder in ascending order

sorted_lotto_set = sorted(lotto_set)
print(sorted_lotto_set)