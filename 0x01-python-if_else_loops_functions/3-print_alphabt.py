#!/usr/bin/python3

# Use a list comprehension to filter out 'q' and 'e'
filtered_alphabet = ''.join([letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter != 'q' and letter != 'e'])

# Print the filtered alphabet without a newline character
print(filtered_alphabet, end='')
