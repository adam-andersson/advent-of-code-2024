import sys

DIRECTIONS = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
}

grid = [list(x.strip()) for x in sys.stdin.readlines()]

seen = set()


def explore(r, c, grid, val):
    if ((r, c)) in seen:
        return False

    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return False

    if not grid[r][c] == val:
        return False

    seen.add((r, c))

    area = set()
    area.add((r, c))
    for dir in DIRECTIONS.values():
        s1 = explore(r + dir[0], c + dir[1], grid, val)
        if s1:
            for a in s1:
                area.add(a)
    return area


def count_perimeter(cells):
    perimeter = 0
    for cell in cells:
        cell_contribution = 4
        for dir in DIRECTIONS.values():
            if (cell[0] + dir[0], cell[1] + dir[1]) in cells:
                cell_contribution -= 1
        perimeter += cell_contribution
    return perimeter


def count_corners(r, c):
    # https://github.com/mgtezak/Advent_of_Code/blob/master/2024/12/p2.py
    NW, W, SW, N, S, NE, E, SE = [
        0 <= r + i < len(grid)
        and 0 <= c + j < len(grid[0])
        and grid[r + i][c + j] == grid[r][c]
        for i in range(-1, 2)
        for j in range(-1, 2)
        if i or j
    ]
    return sum(
        [
            N and W and not NW,
            N and E and not NE,
            S and W and not SW,
            S and E and not SE,
            not (N or W),
            not (N or E),
            not (S or W),
            not (S or E),
        ]
    )


areas = []
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        s = explore(r, c, grid, cell)
        if s:
            areas.append(s)

res1 = sum([len(area) * count_perimeter(area) for area in areas])
print("Part 1:", res1)

res2 = sum([len(area) * sum([count_corners(r, c) for r, c in area]) for area in areas])
print("Part 2:", res2)
