"""
Minesweeper I — Grid
This challenge is based on the game Minesweeper.

Create a function that takes a grid of # and -, where each hash (#) represents
a mine and each dash (-) represents a mine-free spot. Return an array where each
dash is replaced by a digit indicating the number of mines immediately adjacent
to the spot (horizontally, vertically, and diagonally).
"""


def num_grid(grid):
    min_x, min_y, max_x, max_y = 0, 0, len(grid) - 1, len(grid[0]) - 1
    directions = (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)

    def count_mines(x, y):
        count = 0
        for direction_x, direction_y in directions:
            if (
                not (
                    min_x > x + direction_x
                    or x + direction_x > max_x
                    or min_y > y + direction_y
                    or y + direction_y > max_y
                )
                and grid[x + direction_x][y + direction_y] == "#"
            ):
                count += 1
        return str(count)

    return [
        [count_mines(x, y) if row[y] != "#" else "#" for y in range(len(row))]
        for x, row in enumerate(grid)
    ]
