#!/usr/bin/python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    if letter == 'e' or letter == 'q':
        continue
    print(letter, end="")
