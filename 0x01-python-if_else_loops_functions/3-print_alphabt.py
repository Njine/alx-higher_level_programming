#!/usr/bin/python3

# Initialize an empty string
filtered_alphabet = ""

# Iterate through the alphabet and add characters except 'q' and 'e'
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter != 'q' and letter != 'e':
        filtered_alphabet += letter

# Print the filtered alphabet without a newline character
print("{}".format(filtered_alphabet), end="")
