#   1) Create a file handle to open and append to a file called pelican.txt
file_handle = open('pelican.txt', 'w')

# open(file name, mode)         Function opens a file and returns the file object (file handle) via two arguments (file name, mode)
#                               Modes:
#                                 'r': read; allows reading
#                                 'w': write; overwrites the file, will not repeat commands.
#                                 'a': append; data is written to the end of the file, if file ≠ exist, it is created.

# , comma is part of Python syntax to separate parameters in function calls.
# file_handle is a variable that stores the file object returned by open().

#   2) Append lines into the file.
file_handle.write("A wonderful bird is the pelican")
file_handle.write("His bill holds more than his belican\n")

#   3) Create a list that contains sentences from exercise guide and append list to the file.
lines = list("He can take in his beak,\nEnough food for a week,\nBut I'm damned if I see how the helican.\n")
file_handle.writelines(lines)

# .writelines()     is a method that writes a list of strings to a file
# \n                newline is an escape sequence that represents a newline.
#           purpose: ensures each line of text starts on a new line, readability, and helps with structuring, formatting in files.



