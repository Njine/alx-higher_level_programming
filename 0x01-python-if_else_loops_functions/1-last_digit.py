#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
while True:
    digit = abs(number) % 10

    if digit > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, digit))
        break
    elif digit == 0:
        print("Last digit of {} is {} and is 0".format(number, digit))
        break
    else:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, digit))
        break
