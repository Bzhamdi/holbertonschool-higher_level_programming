#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sqr_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return (sqr_matrix)
