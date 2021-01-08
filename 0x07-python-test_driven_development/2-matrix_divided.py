#!/usr/bin/python3
"""Our module that divides elements in a matrix"""


def matrix_divided(matrix, div):
    """Method that divides elements in a matrix
        Args:
            matrix: List of lists of ints
            div: number to divide each int within matrix
        Raises:
            TypeError: when matrix and div not correct type
            ZeroDivisionError: when div is 0
        Returns:
            new matrix with list of the results rounded to 2 dec places
    """
    trixErr = "matrix must be a matrix (list of lists) of integers/floats"
    rowSizeErr = "Each row of the matrix must have the same size"

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    elif div is 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list) is False or len(matrix) is 0:
        raise TypeError(trixErr)

    for row in matrix:
        if len(matrix[0]) is not len(row):
            raise TypeError(rowSizeErr)

        if isinstance(row, list) is False:
            raise TypeError(trixErr)

        for elements in row:
            if isinstance(elements, (int, float)) is False:
                raise TypeError(trixErr)

    return([list(map(lambda x: round(x / div, 2), matrix[row]))
            for row in range(len(matrix))])
