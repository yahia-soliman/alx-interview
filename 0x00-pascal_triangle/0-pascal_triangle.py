#!/usr/bin/python3
"""The factory of Pascal's triangles"""


def pascal_triangle(n):
    """Get a list representing Pascal's triangle of `n`"""
    if n <= 0:
        return []
    level = 1
    prev = [1]
    triangle = [prev]
    while level < n:
        row = [1]
        row.extend([prev[i] + prev[i + 1] for i in range(level - 1)])
        row.append(1)
        triangle.append(row)
        prev = row
        level += 1
    return triangle
