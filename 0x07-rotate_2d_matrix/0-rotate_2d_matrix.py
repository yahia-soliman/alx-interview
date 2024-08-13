#!/usr/bin/python3
"""Rotating 2D Matrix in-place"""


def rotate_2d_matrix(matrix):
    """Rotate `n x n` 2D matrix

    a  b  c       h  e  a
    e  f  g  -->  i  f  b
    h  i  j       j  g  c
    """
    n = len(matrix)

    for x in range(n // 2):
        for y in range(x, n - x - 1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - x - 1] = tmp  # matrix[x][y]
