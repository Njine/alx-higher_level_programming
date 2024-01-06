#!/usr/bin/python3
"""Module for locating peaks in a list of integers."""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = length // 2
    li = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return li[mid]

    if mid - 1 < 0 or li[mid] >= li[mid + 1]:
        return li[mid]
    else:
        return (
            find_peak(li[mid + 1:])
            if li[mid + 1] > li[mid - 1]
            else find_peak(li[:mid])
            )
