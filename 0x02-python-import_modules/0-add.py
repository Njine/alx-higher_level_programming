#!/usr/bin/python3

a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Calculate the result using the imported function
result = add(a, b)

# Print the result with string formatting
print("{} + {} = {}".format(a, b, result))

