import sys

DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}

data = [list(x.strip()) for x in sys.stdin.readlines()]
grid = [[-1 if item == "." else int(item) for item in row] for row in data]

start_coords = []
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 0:
            start_coords.append((r, c))

found_trailtops = set()


def find_trail(r, c, grid, require_distinct, target=0):
    if require_distinct and target == 0:
        found_trailtops.clear()

    val = grid[r][c]
    if val != target:
        return 0
    if val == 9:
        if not require_distinct:
            return 1

        if (r, c) not in found_trailtops:
            found_trailtops.add((r, c))
            return 1
        else:
            return 0

    return sum(
        [
            find_trail(r + dir[0], c + dir[1], grid, require_distinct, val + 1)
            for dir in DIRECTIONS.values()
            if 0 <= r + dir[0] < len(grid) and 0 <= c + dir[1] < len(grid[0])
        ]
    )


for part, require_distinct in zip((1, 2), (True, False)):
    print(
        f"Part {part}:",
        sum(
            [
                find_trail(coords[0], coords[1], grid, require_distinct)
                for coords in start_coords
            ]
        ),
    )
