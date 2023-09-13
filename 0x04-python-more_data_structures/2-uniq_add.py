#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    sum_unique = 0

    for num in my_list:
        if num not in unique_set:
            unique_set.add(num)
            sum_unique += num

    return sum_unique
