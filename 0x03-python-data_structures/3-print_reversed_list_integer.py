#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    reversed_list = list(reversed(my_list))
    
    for integer in reversed_list:
        print("{:d}".format(integer))
