#!/usr/bin/python3

# Use a single loop to print numbers in both decimal and hexadecimal format
for number in range(99):
    print("{} = 0x{:x}".format(number, number))
