import sys

data = sys.stdin.read().splitlines()

res1 = 0
for line in data:
    row = [int(n) for n in line.split(" ")]
    row_asc = sorted(row)
    row_dec = sorted(row, reverse=True)

    if row == row_asc or row == row_dec:
        should_add = True
        for i in range(1, len(row_asc)):
            diff = row_asc[i] - row_asc[i - 1]
            if diff != 1 and diff != 2 and diff != 3:
                should_add = False
                break
        if should_add:
            res1 += 1


print("Part 1:", res1)


res2 = 0

print("Part 2:", res2)
