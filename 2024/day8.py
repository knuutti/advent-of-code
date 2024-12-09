data = open("input_day8.txt",'r').read().splitlines()
from itertools import combinations

ROWS, COLUMNS = len(data), len(data[0])
antennas = {}

for i in range(ROWS):
    for j in range(COLUMNS):
        if data[i][j] != ".":
            if data[i][j] not in antennas:
                antennas[data[i][j]] = [(i,j)]
            else: antennas[data[i][j]].append((i,j))

# SILVER
antinodes = {}
for a in antennas:
    for c in list(combinations(antennas[a], 2)):
        delta = (c[1][0]-c[0][0], c[1][1]-c[0][1])
        a1 = (c[0][0] - delta[0], c[0][1] - delta[1])
        a2 = (c[1][0] + delta[0], c[1][1] + delta[1])
        if a1 in antennas: continue
        if a2 in antennas: continue
        if a1[0] > -1 and a1[0] < ROWS and a1[1] > -1 and a1[1] < COLUMNS: antinodes[a1] = 1
        if a2[0] > -1 and a2[0] < ROWS and a2[1] > -1 and a2[1] < COLUMNS: antinodes[a2] = 1

print("Silver:", len(antinodes))

# GOLD
antinodes = {}
for a in antennas:
    for c in list(combinations(antennas[a], 2)):
        delta = (c[1][0]-c[0][0], c[1][1]-c[0][1])
        multiplier = 0
        while True:
            a = (c[0][0] - multiplier*delta[0], c[0][1] - multiplier*delta[1])
            if a[0] > -1 and a[0] < ROWS and a[1] > -1 and a[1] < COLUMNS: antinodes[a] = 1
            else: break
            multiplier += 1
        multiplier = -1
        while True:
            a = (c[0][0] - multiplier*delta[0], c[0][1] - multiplier*delta[1])
            if a[0] > -1 and a[0] < ROWS and a[1] > -1 and a[1] < COLUMNS: antinodes[a] = 1
            else: break
            multiplier -= 1

print("Gold:", len(antinodes))