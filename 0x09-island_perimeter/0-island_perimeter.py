#!/usr/bin/python3
"""Calculate Island Perimeter"""


def island_perimeter(grid):
    """perimeter of the island described in grid"""
    borders = 0
    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 0:
                continue
            # how many sides around grid[i][j]
            # are connected to water
            borders += 4
            if i > 0:
                borders -= grid[i - 1][j]
            if j > 0:
                borders -= grid[i][j - 1]
            if i < rows - 1:
                borders -= grid[i + 1][j]
            if j < cols - 1:
                borders -= grid[i][j + 1]
    return borders
