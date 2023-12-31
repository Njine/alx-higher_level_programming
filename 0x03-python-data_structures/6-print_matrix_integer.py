#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()
        return

    for row in matrix:
        for i, n in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(n))
            else:
                print("{:d}".format(n), end=" ")
