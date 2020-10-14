#!/usr/bin/env python

f = open("myfile.txt", "w")

# We write this text to the text file
f.write("Hello!")

# Close the text file
f.close()

# Append (i.e. 'a') text to the existing text file
f = open("myfile.txt", "a")

# Here is the text we are appending.
# The '\n' symbol means to put the text on a new line.
f.write("\nNow we have some more text in this file!")
f.close()

# Open and read (i.e. 'r') the file
f = open("myfile.txt", "r")
print(f.read())
