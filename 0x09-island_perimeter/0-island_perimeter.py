#!/usr/bin/python3
"""Calculate Island Perimeter"""


def island_perimeter(grid):
    """perimeter of the island described in grid"""
    borders = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            # ignore sides connected with another [1]
            borders += 4
            if i and grid[i - 1][j]:
                borders -= 2
            if j and grid[i][j - 1]:
                borders -= 2
    return borders
