import sys
import re

data = [x.strip() for x in sys.stdin.readlines()]
rules = set(
    [(int(rule.split("|")[0]), int(rule.split("|")[1])) for rule in data if "|" in rule]
)

series = [
    [int(n) for n in x.split(",")] for x in data if not ("|") in x and not x == ""
]


def validate(v_serie, v_rules, v_n):
    relevant_rules = [r for r in v_rules if v_n in r]
    before = [r[1] for r in relevant_rules if r[0] == v_n]
    after = [r[0] for r in relevant_rules if r[1] == v_n]

    n_idx = v_serie.index(v_n)
    for bef in before:
        if n_idx >= v_serie.index(bef):
            return False
    for aft in after:
        if n_idx <= v_serie.index(aft):
            return False
    return True


res1 = 0
for serie in series:
    filtered_rules = [r for r in rules if (r[0] in serie and r[1] in serie)]

    if all([validate(serie, filtered_rules, n) for n in serie]):
        res1 += serie[int(len(serie) / 2)]

print("Part 1:", res1)

res2 = 0

nums_before_dict = {}
nums_in_series = set()
for a, b in rules:
    nums_in_series.add(a)
    nums_in_series.add(b)
    if a not in nums_before_dict:
        nums_before_dict[a] = set()
    nums_before_dict[a].add(b)


def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        swapped = False
        for i in range(n - 1):
            left, right = arr[i], arr[i + 1]
            if right in nums_before_dict and left in nums_before_dict[right]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


for serie in series:
    filtered_rules = [r for r in rules if (r[0] in serie and r[1] in serie)]

    if all([validate(serie, filtered_rules, n) for n in serie]):
        continue

    sorted_serie = bubble_sort(list(serie))

    res2 += sorted_serie[int(len(sorted_serie) / 2)]


print("Part 2:", res2)
