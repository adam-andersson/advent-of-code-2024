import sys
import re

data = sys.stdin.read()

res1 = sum(
    [int(g[0]) * int(g[1]) for g in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)]
)

print("Part 1:", res1)

muls = {
    g.span()[0]: int(g.groups()[0]) * int(g.groups()[1])
    for g in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", data)
}

do_start_indices = set([g.span()[0] for g in re.finditer(r"do\(\)", data)])
dont_start_indices = set([g.span()[0] for g in re.finditer(r"don't\(\)", data)])

res2 = 0
active = True
for i in range(len(data)):
    if active:
        if i in dont_start_indices:
            active = False
            continue
        if i in muls:
            res2 += muls[i]
    if not active:
        if i in do_start_indices:
            active = True

print("Part 2:", res2)
