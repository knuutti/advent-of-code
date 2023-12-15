# Advent of Code 2023 - Day 14
# Eetu Knutars / @knuutti

def main():
    fname = "./2023/Day 14/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    R = len(data)
    C = len(data[0])

    silver = 0

    r_rocks = [0 for _ in range(C)] # round shaped rocks
    for level,row in enumerate(data[::-1]):
        #print(silver)
        for i,c in enumerate(row):
            #print("Level",level, "Column", i, "Rocks above", r_rocks[i])
            if c == "O":
                r_rocks[i] += 1
            elif c == "#":
                rock_load = sum([x for x in range(level-r_rocks[i]+1,level+1)])
                #print(level, level-r_rocks[i], rock_load)
                silver += rock_load
                #print(rock_load)

                r_rocks[i] = 0
    for i in range(C):
        silver += sum([x for x in range(R-r_rocks[i]+1, R+1)])

    print("Part 1:",silver)


if __name__ == '__main__':
    main()