#!/usr/bin/python3
'''this module contains a function '''


def pascal_triangle(n):
    '''
    a function that returns a list of lists of
    integers representing the Pascal’s triangle of n
    '''

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            # Calculate the binomial coefficient for each position
            coefficient = 1
            if j > 0 and j < i:
                coefficient = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(coefficient)
        triangle.append(row)

    return triangle
