#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Checks if each element in the list is divisible by 2.

    Args:
        my_list (list): The list of integers to check.

    Returns:
        list: A list of Boolean values, check for even values
    """
    return [x % 2 == 0 for x in my_list]
