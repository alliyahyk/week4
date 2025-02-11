#   1) Use open and read to slurp the entire contents of your pelican file.

pelican_file = open('pelican.txt', 'r').read()

# slurping          refers to the practice of reading an entire file or data stream into memory all at once,
#                   rather than processing it line by line or in smaller chunks.
#                   Used to load the entire contents of a file into a single variable.
#                   Small files: efficient –> simplifies code, reduces need for loops.
#                   Large files: inefficient –> consume a lot of memory.

# streaming         The file is processed line by line.

# .read()           reads entire file into a single string.

# .readlines()      reads entire file into a list of strings, where each string represents a line.


#   2) Display the data type and print contents of the returned data.

print(f"Contents of pelican file:\n{pelican_file}")
print(type(pelican_file))
# Data type: string

#   3) Read file into a list and then output the number of items within the list.

pelican_list = open('pelican.txt', 'r').readlines()
print(f"Reading Pelican file as a list:\n{pelican_list}")
print(len(pelican_list))

#   4) Use a loop to iterate over and print the contents of the file.

for line in open('pelican.txt', 'r'):
    print(line.strip())

# .strip() removes the trailing \n from each file when printing. Ensures no blank spaces in the output.
# can slice up to -1
