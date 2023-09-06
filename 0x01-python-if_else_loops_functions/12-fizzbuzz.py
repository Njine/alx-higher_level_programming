#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """Print numbers from 1 to 100 with FizzBuzz replacements."""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(f"{number}", end=" ")
