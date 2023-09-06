#!/usr/bin/python3
# 2-print_alphabet.py

"""Print alphabet in lowercase without a new line."""
print("".join([f"{chr(letter)}" for letter in range(97, 123)]), end="")
