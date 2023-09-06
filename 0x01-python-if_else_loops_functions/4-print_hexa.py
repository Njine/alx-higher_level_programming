#!/usr/bin/python3
import random

# Generate a random number
number = random.randint(-10000, 10000)

# Extract the last digit and handle negative numbers
digit = abs(number) % 10
if number < 0:
    digit = -digit

# Define the output components
output = ["Last digit of", str(number), "is", str(digit), "and is"]

# Determine the last part of the output
if digit > 5:
    output.append("greater than 5")
elif digit == 0:
    output.append("0")
else:
    output.append("less than 6 and not 0")

# Print the formatted output
print(" ".join(output))
