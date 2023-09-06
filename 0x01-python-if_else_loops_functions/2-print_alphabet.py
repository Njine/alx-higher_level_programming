#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet in lowercase, not followed by a new line."""
alphabet = ""
for letter in range(97, 123):
    alphabet += chr(letter)

print(alphabet, end="")
