# Advent of Code 2023 - Day 3
# Eetu Knutars / @knuutti

def main():   
    
    fname = "./2023/Day 03/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    
    file.close()

    numbers = {}
    gears = {}

    for i,line in enumerate(data):
        for j,char in enumerate(line):
            if not char.isnumeric() and char != ".":
                neighbours = get_neigbour_indeces(i,j,len(data)-1, len(line)-1)
                neig = {}
                for neighbour in neighbours:
                    if data[neighbour[0]][neighbour[1]].isnumeric():
                        temp = find_numbers(neighbour[0],neighbour[1], data, len(line)-1)
                        numbers[(temp[0],temp[1])] = temp[2]
                        neig[(temp[0],temp[1])] = temp[2]
                if len(neig) == 2 and char == "*":
                    gear_ratio = 1
                    for n in neig:
                        gear_ratio *= neig[n]
                    gears[(i,j)] = gear_ratio

    

    total = 0
    for num in numbers:
        total += numbers[num]
    print("Part 1:",total)

    total = 0
    for gear in gears:
        total += gears[gear]
    print("Part 2:",total)



def find_numbers(i,j, data, j_max):
    number = int(data[i][j])
    start_j = j
    if j-1 >= 0:
        if data[i][j-1].isnumeric():
            number += 10*int(data[i][j-1])
            start_j -= 1
            if j-2 >= 0:
                if data[i][j-2].isnumeric():
                    number += 100*int(data[i][j-2])
                    start_j -= 1

    if j+1 <= j_max:
        if data[i][j+1].isnumeric():
            number *= 10
            number += int(data[i][j+1])
            if j+2 <= j_max:
                if data[i][j+2].isnumeric():
                    number *= 10
                    number += int(data[i][j+2])
    
    return [i, start_j, number]

def get_neigbour_indeces(i,j, i_max, j_max):
    i_possible = [i]
    if i < i_max:
        i_possible.append(i+1)
    if i > 0:
        i_possible.append(i-1)
    j_possible = [j]
    if j < j_max:
        j_possible.append(j+1)
    if j > 0:
        j_possible.append(j-1)

    neigbour_indeces = []
    for r in i_possible:
        for c in j_possible:
            neigbour_indeces.append([r,c])
    neigbour_indeces.remove([i,j])
    return(neigbour_indeces)



if __name__ == "__main__":
    main()