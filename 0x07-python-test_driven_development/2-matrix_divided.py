#!/usr/bin/python3


'''
    2-matrix_divided.py

    Contains function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor."""

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(
            isinstance(val, (int, float)) for val in row
        ) for row in matrix
    ):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')


    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')


    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')


    if div == 0:
        raise ZeroDivisionError('division by zero')


    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    result = matrix_divided(matrix, 3)
    print(result)
    print(matrix)
