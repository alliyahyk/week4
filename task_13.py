# Task 1: Write a line of code to create a file handle to open and append to a file called pelican.txt
file_handle = open("pelican.txt", "a")
# Append the following line to the file using write method
file_handle.write("A wonderful bird is the pelican,\n")
# Append the following second line using the write method
file_handle.write("His bill holds more than his belican.\n")
# list
lines = ["He can take in his beak,\n", "Enough food for a week,\n","But I'm damned if i can see how the helican.\n"]
file_handle.writelines(lines)
# the \n's are used to create a new line between the setences so they can read on seperate lines.