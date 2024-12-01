import sys

data = sys.stdin.read().splitlines()

l = sorted([int(a) for a, _ in (line.split("   ") for line in data)])
r = sorted([int(b) for _, b in (line.split("   ") for line in data)])

res = 0
for l_i, r_i in zip(l, r):
    res += abs(l_i - r_i)

print(res)
