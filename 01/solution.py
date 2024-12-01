import sys

data = sys.stdin.read().splitlines()

l = sorted([int(a) for a, _ in (line.split("   ") for line in data)])
r = sorted([int(b) for _, b in (line.split("   ") for line in data)])

res = 0
for l_i, r_i in zip(l, r):
    res += abs(l_i - r_i)

print("Part 1:", res)

l_dict = {}
for i in set(l):
    l_dict[i] = l.count(i)

r_dict = {}
for i in set(r):
    r_dict[i] = r.count(i)

res2 = 0
for k, v in l_dict.items():
    if k in r_dict:
        res2 += v * k * r_dict[k]

print("Part 2:", res2)
