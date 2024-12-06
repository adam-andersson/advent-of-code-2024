import sys


def rotate90(dir):
    if dir == directions["N"]:
        return directions["E"]
    if dir == directions["E"]:
        return directions["S"]
    if dir == directions["S"]:
        return directions["W"]
    if dir == directions["W"]:
        return directions["N"]


def find_start(g):
    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == "^":
                return (r, c)


directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}

grid = [list(x.strip()) for x in sys.stdin.readlines()]


i, j = find_start(grid)
direction = directions["N"]

while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
    current = grid[i][j]
    if current == "#":
        i, j = i - direction[0], j - direction[1]
        direction = rotate90(direction)
    else:
        grid[i][j] = "X"
    i, j = i + direction[0], j + direction[1]

res1 = sum([r.count("X") for r in grid])

print("Part 1:", res1)
