import numpy as np
from itertools import combinations

def is_safe(report):
    deltas = np.diff(report)
    if np.max(np.abs(deltas)) > 3 or np.min(np.abs(deltas)) < 1:
        return 0
    elif np.all(np.sign(deltas) == np.sign(deltas)[0]):
        return 1
    return 0

silver, gold = 0, 0
data = [list(map(int, x.split())) for x in open("input_day2.txt").read().splitlines()]

for report in data:
    combs = list(combinations(report, len(report)-1))
    combs.insert(0, report)
    for i,c in enumerate(combs):
        if is_safe(c):
            gold += 1
            if i == 0:
                silver += 1
            break

print("Silver", silver)
print("Gold:", gold)