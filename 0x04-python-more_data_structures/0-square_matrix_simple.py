#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = acpy_matrix.copy()
    for i in range(0, len(matrix)):
        acpy_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        return acpy_matrix
