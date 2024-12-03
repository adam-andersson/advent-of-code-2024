import sys
import re

data = sys.stdin.read()

res1 = sum(
    [int(g[0]) * int(g[1]) for g in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)]
)

print("Part 1:", res1)


# print("Part 2:", res2)
