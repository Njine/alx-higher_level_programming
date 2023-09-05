#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
while True:
    dig = abs(number) % 10

    if number < 0:
        dig = -dig

    if dig > 5:
        print("Last dig of{}is{}and is greater than 5".format(number, dig))
        break
    elif dig == 0:
        print("Last dig of {} is {} and is 0".format(number, dig))
        break
    else:
        print("Last dig of{}is{}and is less than 6 and not 0".format(number, dig))
        break
