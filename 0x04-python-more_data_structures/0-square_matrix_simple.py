#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return([list(map(lambda x: x*x, matrix[row]))
            for row in range(0, len(matrix))])
