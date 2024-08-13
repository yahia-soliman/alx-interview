#!/usr/bin/python3
"""Rotating 2D Matrix in-place"""


def rotate_2d_matrix(matrix):
    """Rotate `n x n` 2D matrix"""
    n = len(matrix)
    copy = [[i for i in row] for row in matrix]
    for i in range(n):
        for j in range(n):
            matrix[j][n - i - 1] = copy[i][j]
