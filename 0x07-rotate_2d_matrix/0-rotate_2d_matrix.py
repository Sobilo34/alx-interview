#!/usr/bin/python3

""" Module to rotate a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    A function that Rotates an n x n 2D
    matrix 90 degrees clockwise in place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

