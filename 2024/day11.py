from math import log10
from collections import defaultdict

def print_counts(stone_counts, mode):
    total = 0
    for s in stone_counts:
        total += stone_counts[s]
    if mode == 1: print("Gold:", total)
    else: print("Silver:", total)

def new_stones(stone):
    if stone == 0:
        return [1]
    stone_len= (int(log10(stone))+1)
    if stone_len % 2 == 0:
        x1 = int(stone // 10**(stone_len/2))
        x2 = int(stone - x1*(10**(stone_len/2)))
        return [x1, x2]
    return [int(2024*stone)]

data = [int(x) for x in open("input_dayb.txt", "r").readline().split()]

# Init counts
stone_counts = defaultdict(int)
for stone in data:
    stone_counts[stone] += 1

transforms = {}
for i in range(75):
    orig_counts = stone_counts.copy()
    for stone in orig_counts:
        stone_counts[stone] -= orig_counts[stone]
        if stone not in transforms:
            stones = new_stones(stone)
            transforms[stone] = stones
        else: stones = transforms[stone]
        for s in stones: 
            stone_counts[s] += orig_counts[stone]

    # Silver
    if i == 24: print_counts(stone_counts, 0)

# Gold
print_counts(stone_counts, 1)


