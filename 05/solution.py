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

print(res1)
