import sys
import math

sys.setrecursionlimit(5000)

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def find(g, char):
    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == char:
                return (r, c)


def move(
    g,
    pos,
    dir,
    cost,
    cost_g,
):
    r, c = pos
    dr, dc = dir

    if not (0 <= r + dr < len(g) and 0 <= c + dc < len(g[0])):
        return False

    if cost >= cost_g[r + dr][c + dc]:
        return False

    if not g[r + dr][c + dc] in [".", "E"]:
        return False

    cost_g[r + dr][c + dc] = cost

    # straight
    move(g, (r + dr, c + dc), dir, cost + 1, cost_g)

    # rotate 90
    move(g, (r + dr, c + dc), (dc, -dr), cost + 1001, cost_g)

    # rotate -90
    move(g, (r + dr, c + dc), (-dc, dr), cost + 1001, cost_g)


grid = [[x for x in l.strip()] for l in sys.stdin.readlines()]
costs = [[math.inf for _ in row] for row in grid]

source = find(grid, "S")
costs[source[0]][source[1]] = 0

move(grid, source, DIRECTIONS[">"], 1, costs)
move(grid, source, DIRECTIONS["^"], 1001, costs)
move(grid, source, DIRECTIONS["v"], 1001, costs)

sink = find(grid, "E")
print("Part 1:", costs[sink[0]][sink[1]])
