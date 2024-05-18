#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix..
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix and return a list(s)

    Args:
        matrix: Must be a list of lists of integers or floats.
                Each row of the matrix must be of the same size.
        div: Must be a number(integer or float).
             It cannot be equal to zero.


    Returns:
        A list of a new matrix and rounded to two decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If each row of the size of a matrix is not of the same size.
    TypeError: If div is not an integer or float.
    ZeroDivisionError: If div is equal to zero.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
