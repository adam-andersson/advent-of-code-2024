import sys

grid = [list(x.strip()) for x in sys.stdin.readlines()]

antenna_frequencies = {}
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell.isalnum():
            if not cell in antenna_frequencies:
                antenna_frequencies[cell] = set()
            antenna_frequencies[cell].add((r, c))

mirror_positions = set()
max_row = len(grid)
max_col = len(grid[0])
for frequency, positions in antenna_frequencies.items():
    for idx_origin, position in enumerate(positions):
        for idx_resonator, position_resonator in enumerate(positions):
            if idx_resonator == idx_origin:
                continue

            diff_row, diff_col = (
                position[0] - position_resonator[0],
                position[1] - position_resonator[1],
            )

            mirror_row, mirror_col = (position[0] + diff_row, position[1] + diff_col)

            if 0 <= mirror_row < max_row and 0 <= mirror_col < max_col:
                mirror_positions.add((mirror_row, mirror_col))

print("Part 1:", len(mirror_positions))


mirror_positions = set()
max_row = len(grid)
max_col = len(grid[0])
for frequency, positions in antenna_frequencies.items():
    for idx_origin, position in enumerate(positions):
        for idx_resonator, position_resonator in enumerate(positions):
            if idx_resonator == idx_origin:
                continue

            diff_row, diff_col = (
                position[0] - position_resonator[0],
                position[1] - position_resonator[1],
            )

            mirror_positions.add((position_resonator[0], position_resonator[1]))

            mirror_row, mirror_col = (position[0] + diff_row, position[1] + diff_col)
            while 0 <= mirror_row < max_row and 0 <= mirror_col < max_col:
                grid[mirror_row][mirror_col] = "#"
                mirror_positions.add((mirror_row, mirror_col))
                mirror_row, mirror_col = mirror_row + diff_row, mirror_col + diff_col

print("Part 2:", len(mirror_positions))
# for rowww in grid:
#     print(rowww)
