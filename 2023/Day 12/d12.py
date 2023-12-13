# Advent of Code 2023 - Day 12
# Eetu Knutars / @knuutti

# Solved part 1 only :(

def main():
    fname = "./2023/Day 12/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    counter = 0
    for i,row in enumerate(data):
        row, groups = parse_data(row, 0)
        counter += get_counts(row, groups)

    print("Part 1:", counter)

def parse_data(row, mode):
    row = row.split()
    groups = [int(x) for x in (row[1]).split(',')]
    row = row[0]
    if mode:
        row = row + 4*("?" + row)
        g = groups.copy()
        for _ in range(4):
            groups.extend(g)
    #print(row, groups)
    return row, groups

def get_counts(row: str, groups: list):
    if row.count("?") + row.count("#") < sum(groups):
        return 0
    #print(row)
    if not row.count("?"): # no more unknowns
        broken = row.replace(".", " ").split()
        lens = [len(x) for x in broken]
        if lens == groups:
            #print("Possible! OwO")
            return 1
        return 0

    # Checking if the given grouping is still possible
    potential_groups = row.replace(".", " ").split()
    #print(potential_groups)
    for i,g in enumerate(potential_groups):
        #print(i, g, groups)
        if i >= len(groups):
            if potential_groups[i].count("#"):
                return 0
            #print("öalkdj")
            get_counts(row.replace("?", "."), groups)
        else:
            if len(g) < groups[i] and g.count("#"): # impossible to form required group
                #print("sadöjf")
                return 0
            
            
            if g.count("?"): # still unknowns, don't do anything
                break
            if len(g) != groups[i]: # impossible combination
                return 0
    index = row.find("?")
    return get_counts(row[:index] + "#" + row[index+1:], groups) + get_counts(row[:index] + "." + row[index+1:], groups)


if __name__ == '__main__':
    main()
