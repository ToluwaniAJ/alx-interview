#!/usr/bin/python3
"""This file attempt to solve the island perimeter question"""


def island_perimeter(grid):
    """This finds the perimeter of an island"""
    perimeter = 0
    x = len(grid)
    for i in range(x):
        m = len(grid[i])
        for j in range(m):
            if grid[i][j] == 1:
                if (i - 1 >= 0 and grid[i - 1][j] == 0) or i == 0:
                    perimeter += 1
                if (i + 1 < x and grid[i + 1][j] == 0) or i == (x - 1):
                    perimeter += 1
                if (j - 1 >= 0 and grid[i][j - 1] == 0) or j == 0:
                    perimeter += 1
                if (j + 1 < m and grid[i][j + 1] == 0) or j == (m - 1):
                    perimeter += 1
    return perimeter