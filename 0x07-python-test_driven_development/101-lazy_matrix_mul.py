#!/usr/bin/python3
"""Define matrix factorial function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the factorial of two matrices."""

    return (np.matmul(m_a, m_b))
