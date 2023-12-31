#!/usr/bin/python3

"""Define a matrix factorial function."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, contains non-integer/float elements,
                   or has rows of different sizes.
        ValueError: If m_a or m_b is empty or cannot be multiplied.

    Example:
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[7, 10], [15, 22]]
        >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        [[13, 16]]
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            prod = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            row.append(prod)
        result.append(row)

    return result

if __name__ == "__main__":
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
