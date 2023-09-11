#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        i = 0
        while i < len(my_list):
            if i == idx:
                my_list[i] = element
                break
            i += 1
    return my_list
