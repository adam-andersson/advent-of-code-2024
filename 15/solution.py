import sys

DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def find_start(g):
    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == "@":
                return (r, c)


def push(g, r, c, dr, dc):
    while g[r][c] == "O":
        if g[r + dr][c + dc] == ".":
            return (r + dr, c + dc)
        elif g[r + dr][c + dc] == "#":
            return False
        r += dr
        c += dc
    if abs(r) + abs(c) == 1:
        return False

    raise SyntaxError()


def coordinates(g):
    coordinate_s = set()
    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == "O":
                coordinate_s.add((r, c))
    return coordinate_s


data = [l.strip() for l in sys.stdin.readlines()]

grid, instructions = [list(x) for x in data[: data.index("")]], "".join(
    data[data.index("") + 1 :]
)

pos = find_start(grid)

for instr in instructions:
    di, dj = DIRECTIONS[instr][0], DIRECTIONS[instr][1]
    instruction_pos = (pos[0] + di, pos[1] + dj)

    char_at_pos = grid[instruction_pos[0]][instruction_pos[1]]
    if char_at_pos == "#":
        continue
    elif char_at_pos == ".":
        pass
    else:
        pushed = push(grid, instruction_pos[0], instruction_pos[1], di, dj)
        if not pushed:
            continue
        else:
            grid[pushed[0]][pushed[1]] = "O"

    grid[pos[0]][pos[1]] = "."
    pos = instruction_pos
    grid[pos[0]][pos[1]] = "@"

coords = coordinates(grid)
res1 = sum([100 * c[0] + c[1] for c in list(coords)])

print("Part 1:", res1)
