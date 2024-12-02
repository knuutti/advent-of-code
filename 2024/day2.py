import numpy as np
from itertools import combinations

def is_safe(report):
    deltas = np.diff(report)
    return np.all([i in [1,2,3] for i in np.abs(deltas)]) and np.all(np.sign(deltas) == np.sign(deltas)[0])

silver, gold = 0, 0
data = [list(map(int, x.split())) for x in open("input_day2.txt").read().splitlines()]

for report in data:
    combs = list(combinations(report, len(report)-1))
    combs.insert(0, report)
    for i,comb in enumerate(combs):
        if is_safe(comb):
            silver += 1*(i==0)
            gold += 1
            break

print("Silver", silver)
print("Gold:", gold)