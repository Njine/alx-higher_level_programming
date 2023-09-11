#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    
    # Iterate through the list in reverse and print each integer
    for integer in reversed(my_list):
        print("{:d}".format(integer))
