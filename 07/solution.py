import sys


data = [[l.strip() for l in line.split(":")] for line in sys.stdin.read().splitlines()]
parsed_data = [(int(l[0]), list(map(int, l[1].split(" ")))) for l in data]


def run_equation(op, eq, acc, target, part2=False):
    eq = eq[:]
    if len(eq) == 0 or acc > target:
        if acc == target:
            return True
        return False

    value = eq.pop(0)

    if op == "+":
        acc += value
    elif op == "*":
        acc *= value
    elif op == "||":
        acc = int(str(acc) + str(value))

    return any(
        [
            run_equation("+", eq, acc, target, part2),
            run_equation("*", eq, acc, target, part2),
            part2 & run_equation("||", eq, acc, target, part2),
        ]
    )


res1, res2 = 0, 0
for looking_for, equation in parsed_data:
    if any(
        [
            run_equation("+", equation, 0, looking_for),
            run_equation("*", equation, 0, looking_for),
        ]
    ):
        res1 += looking_for
        res2 += looking_for
    elif any(
        [
            run_equation("+", equation, 0, looking_for, True),
            run_equation("*", equation, 0, looking_for, True),
            run_equation("||", equation, 0, looking_for, True),
        ]
    ):
        res2 += looking_for

print("Part 1:", res1)
print("Part 2:", res2)
