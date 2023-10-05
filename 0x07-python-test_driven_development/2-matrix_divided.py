#!/usr/bin/python3


'''
    2-matrix_divided.py

    Contains function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix, should be a list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if the rows of the matrix have different sizes,
                   if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Check if all rows have the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide the elements of the matrix and round to 2 decimal places
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
