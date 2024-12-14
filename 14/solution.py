import sys

data = [l.strip() for l in sys.stdin.readlines()]


def move_robot(r, c, v, moves_remaining, max_r, max_c):
    if moves_remaining == 0:
        return (r, c)
    new_r = (r + v[1]) % max_r
    new_c = (c + v[0]) % max_c
    return move_robot(new_r, new_c, v, moves_remaining - 1, max_r, max_c)


def get_quadrant(r, c, max_r, max_c):
    if r == max_r // 2 or c == max_c // 2:
        return False

    if r < max_r // 2:
        y = "N"
    else:
        y = "S"
    if c < max_c // 2:
        x = "W"
    else:
        x = "E"
    return y + x


ROWS = 103
COLS = 101
TIME = 100
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
quads = {"NW": 0, "NE": 0, "SW": 0, "SE": 0}

for robot_data in data:
    robot_count, y = tuple(
        map(
            int,
            "".join(
                [c for c in robot_data.split(" ")[0] if c.isdigit() or c == ","]
            ).split(","),
        )
    )

    vel = tuple(
        map(
            int,
            "".join(
                [
                    c
                    for c in robot_data.split(" ")[1]
                    if c.isdigit() or c == "-" or c == ","
                ]
            ).split(","),
        )
    )

    final_position = move_robot(y, robot_count, vel, TIME, ROWS, COLS)
    grid[final_position[0]][final_position[1]] += 1
    quad = get_quadrant(final_position[0], final_position[1], ROWS, COLS)

    if quad:
        quads[quad] += 1

res1 = 1
for robot_count in quads.values():
    res1 *= robot_count

print("Part 1:", res1)
