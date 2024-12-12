import sys


data = list(map(int, list(sys.stdin.read().strip())))


# print(data)

expanded = []
i, l = 0, 0
while l < len(data):
    if l % 2 == 0:
        for _ in range(data[l]):
            expanded.append(str(i))
        i += 1
    else:
        for _ in range(data[l]):
            expanded.append(".")

    l += 1

compacted = []
l, r = 0, len(expanded) - 1
for i, char in enumerate(expanded):
    if char.isalnum():
        compacted.append(".")
        continue
    while not expanded[r].isalnum():
        r -= 1
    if len(compacted) < r:
        compacted.append(expanded[r])
        expanded[r] = "."
    else:
        break


# print("".join(expanded))
# print("".join(compacted))
# print("0099811188827773336446555566..............")

res1 = 0
for i, (a, b) in enumerate(zip(expanded, compacted)):
    c = 0
    if a.isalnum():
        if b.isalnum():
            raise ValueError
        c = int(a)
    elif b.isalnum():
        c = int(b)
    else:
        raise ValueError

    res1 += i * c

print(res1)
