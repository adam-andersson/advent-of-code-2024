import sys

DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}

START_DIRECTION = DIRECTIONS["N"]


def rotate90(dir):
    if dir == DIRECTIONS["N"]:
        return DIRECTIONS["E"]
    if dir == DIRECTIONS["E"]:
        return DIRECTIONS["S"]
    if dir == DIRECTIONS["S"]:
        return DIRECTIONS["W"]
    if dir == DIRECTIONS["W"]:
        return DIRECTIONS["N"]


def find_start(g):
    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == "^":
                return (r, c)


def grid_walk(g, pos, dir, recurse=False, rec_pos=(0, 0)):
    seen = {}
    i, j = pos
    while 0 <= i < len(g) and 0 <= j < len(g[0]):
        current = g[i][j]
        if current == "#":
            i, j = i - dir[0], j - dir[1]
            dir = rotate90(dir)
        else:
            if not (i, j) in seen:
                seen[(i, j)] = set()
            elif dir in seen[(i, j)]:
                obstacles.add(rec_pos)
                return
            seen[(i, j)].add(dir)

            if recurse:
                g_copy = [row[:] for row in g]
                g_copy[i][j] = "#"
                grid_walk(g_copy, pos, DIRECTIONS["N"], False, (i, j))

        i, j = i + dir[0], j + dir[1]
    return len(seen)


grid = [list(x.strip()) for x in sys.stdin.readlines()]
obstacles = set()

res1 = grid_walk(grid, find_start(grid), START_DIRECTION)
_res2 = grid_walk(grid, find_start(grid), START_DIRECTION, True)

print("Part 1:", res1)
print("Part 2:", len(obstacles))
