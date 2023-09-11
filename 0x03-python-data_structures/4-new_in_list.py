#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        new_list = my_list.copy()  # Create a shallow copy of the original list
        new_list[idx] = element
        return new_list
    return my_list  # Return the original list if the index is out of bounds
