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


def find_cost(cells):
    perimeter = 0
    for cell in cells:
        cell_contribution = 4
        for dir in DIRECTIONS.values():
            if (cell[0] + dir[0], cell[1] + dir[1]) in cells:
                cell_contribution -= 1
        perimeter += cell_contribution
    return perimeter * len(cells)


areas = []
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        s = explore(r, c, grid, cell)
        if s:
            areas.append(s)

res1 = sum([find_cost(area) for area in areas])
print("Part 1:", res1)
