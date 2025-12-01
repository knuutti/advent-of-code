data = open("input_day4.txt", 'r').read().splitlines()

R = len(data)
C = len(data[0])
total = 0
for i in range(1,R-1):
    for j in range(1,C-1):
        if data[i][j] != "A":
            continue    
        diags = [0,0]
        if (data[i+1][j+1] == "S" and data[i-1][j-1] == "M") or (data[i+1][j+1] == "M" and data[i-1][j-1] == "S"):
            if (data[i-1][j+1] == "S" and data[i+1][j-1] == "M") or (data[i-1][j+1] == "M" and data[i+1][j-1] == "S"):
                total += 1

print(R,C)
print(total)
