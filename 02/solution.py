import sys

data = sys.stdin.read().splitlines()


def validate(r):
    row_asc = sorted(r)
    row_dec = sorted(r, reverse=True)

    if r == row_asc or r == row_dec:
        for i in range(1, len(row_asc)):
            diff = row_asc[i] - row_asc[i - 1]
            if not diff in {1, 2, 3}:
                return False
        return True


res1 = 0
for line in data:
    row = [int(n) for n in line.split(" ")]
    res1 += 1 if validate(row) else 0

print("Part 1:", res1)

res2 = 0
for line in data:
    row = [int(n) for n in line.split(" ")]
    res2 += 1 if any([validate(row[:i] + row[i + 1 :]) for i in range(len(row))]) else 0

print("Part 2:", res2)
