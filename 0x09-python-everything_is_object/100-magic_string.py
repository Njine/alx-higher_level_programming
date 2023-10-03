#!/usr/bin/python3
def magic_string(list=[0]):
    list[0] += 1
    return "BestSchool, " * (list[0] - 1) + "BestSchool"