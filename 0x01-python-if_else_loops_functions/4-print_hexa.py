#!/usr/bin/python3
# 4-print_hexa.py

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for number in range(99):
    print("{} = 0x{:02x}".format(number, number))
