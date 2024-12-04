import sys
import re

data = sys.stdin.read()

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
    "NW": (-1, -1),
    "NE": (-1, 1),
    "SW": (1, -1),
    "SE": (1, 1),
}

MAGIC_WORD = "XMAS"

rows = data.strip().split("\n")
grid = [[c for c in r] for r in rows]


def check_cell(cell_y, cell_x, dir, expected_i):
    current_cell = grid[cell_y][cell_x]
    if not current_cell == MAGIC_WORD[expected_i]:
        return False
    if current_cell == MAGIC_WORD[expected_i] and current_cell == MAGIC_WORD[-1]:
        return True
    potential_new_y = cell_y + dir[0]
    potential_new_x = cell_x + dir[1]
    if 0 <= potential_new_y < len(grid) and 0 <= potential_new_x < len(grid[0]):
        return check_cell(potential_new_y, potential_new_x, dir, expected_i + 1)
    else:
        return False


res1 = 0
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if not cell == MAGIC_WORD[0]:
            continue
        res1 += sum([check_cell(r, c, dir, 0) for dir in directions.values()])

print("Part 1:", res1)

res2 = None
print("Part 2:", res2)
