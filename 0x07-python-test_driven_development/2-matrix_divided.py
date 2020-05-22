#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements"""
    len_test = len(matrix[0])
    matrix_final = []
    lst = []
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if len(matrix[i]) != len_test:
            raise TypeError("Each row of the matrix must have the same size")
        if type(matrix[i]) != list:
            raise TypeError(err)
        lst = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != float and type(matrix[i][j]) != int:
                raise TypeError(err)
            if div == float('inf'):
                lst.append(round(0 / 1, 2))
            else:
                lst.append(round(matrix[i][j] / div, 2))
        matrix_final.append(lst)
    return (matrix_final)
