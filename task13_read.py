# Using the open and read methods to slurp the entire contents of pelican.txt
reading_file = open('pelican.txt', 'r').read()
# Slurping: the {} is slurping the entire content from pelican.txt
print(f"This is the pelican file content:\n{reading_file}")

# type?
print(type(reading_file))

# Slurping as a list using .readlines() method to use multiple lines/strings as a list
pelican_list = open('pelican.txt', 'r').readlines()
print(f'This is the pelican file as a list:\n{pelican_list}')

# for loop opening file
for line in open('pelican.txt', 'r'):
    # printing the output and removing line spaces with .strip() method
    print(line.strip())


