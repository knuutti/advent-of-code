data = open("input_dayd.txt").read().splitlines()

import numpy as np

# Data parsing
# Not pretty, could use regex...
counter = 0
A = []
B = []
P = [] # price
for row in data:
    if counter % 4 == 0:
        temp = row.split("X+")
        temp = temp[1].split(", Y+")
        A.append(np.matrix([int(temp[0]), int(temp[1])]))
    elif counter % 4 == 1:
        temp = row.split("X+")
        temp = temp[1].split(", Y+")
        B.append(np.matrix([int(temp[0]), int(temp[1])]))
    elif counter % 4 == 2:
        temp = row.split("X=")
        temp = temp[1].split(", Y=")
        P.append(np.matrix([int(temp[0]), int(temp[1])]).T)
    counter += 1

# Actual solution
# Linear algebra is my goat
silver, gold = 0, 0
N = len(P)
for i in range(N):
    K = np.concat([A[i],B[i]]).T
    Kinv = np.linalg.inv(K)
    price_silver = P[i]
    price_gold = P[i] + 10000000000000
    moves_silver = np.round(Kinv @ price_silver)
    moves_gold = np.round(Kinv @ price_gold)
    if (np.all(K @ moves_silver == price_silver)):
        if np.max(moves_silver) < 100:
            cost = moves_silver[0]*3 + moves_silver[1]
            silver += round(cost[0,0])
    if (np.all(K @ moves_gold == price_gold)):
        cost = moves_gold[0]*3 + moves_gold[1]
        gold += round(cost[0,0])

print("Silver:", silver)
print("Gold:", gold)
            
