data = open("input_day4.txt", 'r').read().splitlines()

R = len(data)
C = len(data[0])
silver = 0
conditions = {"U": False, "D": False, "L": False, "R": False}
for i in range(R):
    for j in range(C):
        if data[i][j] != "X":
            continue
        if i > 2:
            # north
            if data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
                silver += 1
            if j > 2:
                # north-west
                if data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
                    silver += 1
            if j < C-3:
                # north-east
                if data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
                    silver += 1
        if j < C-3:
            # east
            if data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
                silver += 1
        if j > 2:
            # west
            if data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
                silver += 1
        if i < R-3:
            # south
            if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
                silver += 1
            if j > 2:
                # south-west
                if data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
                    silver += 1
            if j < C-3:
                # south-east
                if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                    silver += 1

gold = 0
for i in range(1,R-1):
    for j in range(1,C-1):
        if data[i][j] != "A":
            continue    
        diags = [0,0]
        if (data[i+1][j+1] == "S" and data[i-1][j-1] == "M") or (data[i+1][j+1] == "M" and data[i-1][j-1] == "S"):
            if (data[i-1][j+1] == "S" and data[i+1][j-1] == "M") or (data[i-1][j+1] == "M" and data[i+1][j-1] == "S"):
                gold += 1

print("Silver:", silver)
print("Gold:", gold)