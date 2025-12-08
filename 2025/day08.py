import numpy as np
import pandas as pd

points = pd.read_csv("day08.csv", header=None).to_numpy()

N,_ = np.shape(points)

circuit_indeces = np.linspace(1,N, N)

def euclidian_distance(p1, p2):
    return np.sqrt(np.sum(np.square(p1-p2)))

possible_connections = {}
for i in range(N-1):
    for j in range(i+1,N):
        possible_connections[(i,j)] = euclidian_distance(points[i,:], points[j,:])

wanted_connections = 1000

for i,x in enumerate(sorted(possible_connections, key=lambda x: possible_connections[x])):
    # iterating possible connections based on distance
    # connect points if they are not in the same circuit

    i,j = x[0], x[1]
    ci, cj = circuit_indeces[i], circuit_indeces[j]

    #if ci != cj:
    circuit_indeces[np.where(circuit_indeces == cj)[0]] = ci
    wanted_connections -= 1

    _,counts = np.unique(circuit_indeces, return_counts=True)
    if wanted_connections == 0: 
        print("Silver:", np.prod(np.sort(counts)[-3:]))

    if len(counts) == 1: 
        print("Gold:", points[i,0] * points[j,0])
        break

