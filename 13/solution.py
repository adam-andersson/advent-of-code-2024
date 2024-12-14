import sys

data = [x.strip() for x in sys.stdin.readlines()]


# 8400 = 94 * a + 22 * b
# 5400 = 34 * a + 67 * b


def solve_lin_eq(eq1, eq2):
    # eliminate b
    eq3, eq4 = (
        (eq1[0] * eq2[1], eq1[1] * eq2[1], eq1[2] * eq2[1]),
        (eq2[0] * eq1[1], eq2[1] * eq1[1], eq2[2] * eq1[1]),
    )

    eq5 = (eq3[0] - eq4[0], eq3[1] - eq4[1], eq3[2] - eq4[2])
    a = eq5[2] / eq5[0]

    if a % 1 != 0:
        return False

    a = int(a)
    b = (eq1[2] - a * eq1[0]) / eq1[1]

    if b % 1 != 0:
        return False
    b = int(b)

    return a, b


res1, res2 = 0, 0
for i in range(0, len(data), 4):
    a_btn = tuple(map(int, [x.split("+")[-1] for x in data[i].split(", ")]))
    b_btn = tuple(map(int, [x.split("+")[-1] for x in data[i + 1].split(", ")]))
    target1, target2 = tuple(
        map(int, [x.split("=")[-1] for x in data[i + 2].split(", ")])
    )

    for part in (1, 2):
        solution = solve_lin_eq(
            (a_btn[0], b_btn[0], target1 + (0 if part == 1 else 10000000000000)),
            (a_btn[1], b_btn[1], target2 + (0 if part == 1 else 10000000000000)),
        )

        if solution:
            if part == 1:
                res1 += solution[0] * 3 + solution[1]
            elif part == 2:
                res2 += solution[0] * 3 + solution[1]

print("Part 1:", res1)
print("Part 2:", res2)
