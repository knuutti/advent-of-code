fname = "day07.txt"
file = open(fname, 'r')

data = file.read().splitlines()

start_index = data[0].index("S")

splits = 0

C = len(data[0])
data.pop(0)
N = len(data)

curr = [False] * C

curr[start_index] = True

beams = [0] * C
beams[start_index] = 1

for j in range(1, N, 2):
    row = data[j]
    prev = curr.copy()
    new_beams = [0] * C
    for i in range(1,C-1):
        if prev[i] and row[i] == "^":
            curr[i-1], curr[i], curr[i+1] = True, False, True
            splits += 1
            new_beams[i-1] += beams[i]
            new_beams[i+1] += beams[i]
        elif prev[i]:
            new_beams[i] += beams[i]

    beams = new_beams

        
print("Silver:", splits)
print("Gold:", sum(beams))
