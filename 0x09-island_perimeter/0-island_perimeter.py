#!/usr/bin/python3
"""
This script defines a function that calculates the perimeter of an island
described by a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in the grid.

    Args:
    - grid (list of list of int): A 2D grid representing the island.

    Returns:
    - int: The perimeter of the island.
    """
    perimeter = 0
    grid_length = len(grid)

    for row in range(grid_length):
        for column in range(len(grid[row])):
            # Check if the current cell is part of the island
            if grid[row][column] == 1:
                # Check left neighbor
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                # Check top neighbor
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                # Check right neighbor
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if row + 1 >= grid_length or grid[row + 1][column] == 0:
                    perimeter += 1

    return perimeter
