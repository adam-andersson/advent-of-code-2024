import sys

data = sys.stdin.read().splitlines()

left = sorted([int(a) for a, _ in (line.split("   ") for line in data)])
right = sorted([int(b) for _, b in (line.split("   ") for line in data)])

res1 = sum(abs(l - r) for l, r in zip(left, right))

print("Part 1:", res1)

l_dict = {n: left.count(n) for n in set(left)}
r_dict = {n: right.count(n) for n in set(right)}

res2 = sum(v * k * r_dict[k] for k, v in l_dict.items() if k in r_dict)

print("Part 2:", res2)
