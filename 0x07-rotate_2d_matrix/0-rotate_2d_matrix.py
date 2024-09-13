#!/usr/bin/python3
"""
Function to rotate a matrix
"""


def rotate_2d_matrix(matrix):
    """
    function to transpose a matrix
    """
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(size):
        matrix[i].reverse()
