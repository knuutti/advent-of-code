# Advent of Code 2023 - Day 10
# Eetu Knutars / @knuutti

# Slightly more complicated than the previous day

def main():   
    fname = "./2023/Day 11/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    expanded_data = []

    N = 1000000

    for row in data:
        if "#" not in row:
            expanded_data.append(row.replace(".", "x"))
            continue
        expanded_data.append(row)

    columns = []
    for j in range(0,len(data[0])):
        for i in range(0, len(data)):
            galaxy = False
            if data[i][j] == "#":
                galaxy = True
                break
        if not galaxy:
            columns.append(j)

    #print(expanded_data)

    for c in sorted(columns, reverse=True):
        #print(c)
        for i in range(0,len(expanded_data)):
            #print(expanded_data[i])
            expanded_data[i] = expanded_data[i][0:c] + "x" +  expanded_data[i][c+1:len(expanded_data[i])]
            #print(expanded_data[i])

    # Analysis

    galaxies = []
    for i in range(0,len(expanded_data)):
        for j in range(0,len(expanded_data[0])):
            if expanded_data[i][j] == "#":
                galaxies.append([i,j])

    #print

    #print(galaxies)

    distances = 0

    for i in range(0,len(galaxies)):
        for j in range(i+1,len(galaxies)):
            counter = 0
            dy = -galaxies[i][0]+galaxies[j][0]
            dx = -galaxies[i][1]+galaxies[j][1]
            distances += abs(dy) + abs(dx)
            if dy > 0:
                for ii in range(galaxies[i][0]+1,galaxies[j][0]):
                    if expanded_data[ii][galaxies[i][1]] == "x":
                        counter += 1
            elif dy < 0:
                for ii in range(galaxies[j][0]+1,galaxies[i][0]):
                    if expanded_data[ii][galaxies[i][1]] == "x":
                        counter += 1
            if dx > 0:
                for jj in range(galaxies[i][1]+1,galaxies[j][1]):
                    if expanded_data[galaxies[i][0]][jj] == "x":
                        counter += 1
            elif dx < 0:
                for jj in range(galaxies[j][1]+1,galaxies[i][1]):
                    if expanded_data[galaxies[i][0]][jj] == "x":
                        counter += 1
            
            distances += (N-1)*counter

            #print(galaxies[i], galaxies[j], distances)


    print(distances)



if __name__ == "__main__":
    main()