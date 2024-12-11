from math import log10

def new_stones(stone):
    if stone == 0:
        return [1]
    stone_len= (int(log10(stone))+1)
    if stone_len % 2 == 0:
        x1 = int(stone // 10**(stone_len/2))
        x2 = int(stone - x1*(10**(stone_len/2)))
        return [x1, x2]
    return [int(2024*stone)]

data = open("input_dayb.txt", "r").readline().split()
data = [int(x) for x in data]

orig_list = data
new_list = []
transforms = {}
lens = []

# Init counts
stone_counts = {}
for stone in orig_list:
    if stone not in stone_counts: stone_counts[stone] = 1
    else: stone_counts[stone] += 1

for i in range(75):
    orig_counts = stone_counts.copy()
    for stone in orig_counts:
        stone_counts[stone] -= orig_counts[stone]
        if stone not in transforms:
            stones = new_stones(stone)
            transforms[stone] = stones
        else: stones = transforms[stone]
        for s in stones: 
            if s not in stone_counts:
                stone_counts[s] = orig_counts[stone]
            else: stone_counts[s] += orig_counts[stone]
        
    
    if i==24:
        silver = 0
        for s in stone_counts:
            silver += stone_counts[s]
        print("Silver:", silver)

gold = 0
for s in stone_counts:
    gold += stone_counts[s]
print("Gold:", gold)


