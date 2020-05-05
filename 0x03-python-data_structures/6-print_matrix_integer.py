#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    for i in range(r):
        k = len(matrix[i])
        for j in range(k):
            if j < k - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]), end='')
        print()
