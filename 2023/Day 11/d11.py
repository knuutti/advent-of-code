# Advent of Code 2023 - Day 10
# Eetu Knutars / @knuutti

# Slightly more complicated than the previous day

def main():   
    fname = "./2023/Day 11/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    expanded_data = []

    for row in data:
        expanded_data.append(row)
        if "#" not in row:
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
            expanded_data[i] = expanded_data[i][0:c] + "." +  expanded_data[i][c:len(expanded_data[i])]
            #print(expanded_data[i])

    galaxies = []
    for i in range(0,len(expanded_data)):
        for j in range(0,len(expanded_data[0])):
            if expanded_data[i][j] == "#":
                galaxies.append([i,j])

    print(galaxies)

    distances = 0
    for i in range(0,len(galaxies)):
        for j in range(i,len(galaxies)):
            distances += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])

    print(distances)



if __name__ == "__main__":
    main()