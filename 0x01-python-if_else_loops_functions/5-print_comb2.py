#!/usr/bin/python3
# 5-print_comb2.py

for number in range(100):
    separator = ", " if number < 99 else ""
    print(f"{number:02}{separator}", end="")

print()
 