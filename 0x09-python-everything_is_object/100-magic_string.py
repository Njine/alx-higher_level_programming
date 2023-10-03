#!/usr/bin/python3

def magic_string(iteration=[0]):
    iteration[0] += 1
    return "BestSchool, " * (iteration[0] - 1) + "BestSchool"

for i in range(10):
    print(magic_string())

