#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[1, 2, 3]]
print(matrix_divided(matrix))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, float('inf')))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, 3))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, 2))

matrix = [[1, "ha", 3], [4, 5, 6]]
print(matrix_divided(matrix, 2))

matrix = [[1.2, 2.6, 3.3], [4.2, 5.7, 6.33]]
print(matrix_divided(matrix, 3))

matrix = [[1, 2, 3], [4.2, 5, 6.33]]
print(matrix_divided(matrix, 3))

matrix = [[1, 2, 3], [4, 5, 6, 7]]
print(matrix_divided(matrix, 3))

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, 0))

matrix = [[1, "ha", 3], [4, 5, 6]]
print(matrix_divided(matrix, 2))
