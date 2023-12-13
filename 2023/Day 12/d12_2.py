def main():
    fname = "./2023/Day 12/example.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    #counter = 0
    for i,row in enumerate(data[0:1]):
        #print(i+1)
        row, _ = parse_data(row, 0)
        #counter += get_counts(row, groups)
        combs, known = get_combinations(row, {})
        print(known)
        
    #print(counter)


def get_combinations(row: str, known: dict):
    #print(row)
    groups = row.replace(".", " ").split()
    combs = []
    for group in groups:
        if group in known:
            continue
        combs = []
        print(group)
        if not group.count("?"):
            known[group] = len(group)
            combs = [len(group)]

        elif group not in known:
            index = group.find("?")
            combs1, known = get_combinations(group[:index] + "." + group[index+1:], known)
            combs2, known = get_combinations(group[:index] + "#" + group[index+1:], known)
            combs1.extend(combs2)
            combs.append(combs1)
            known[group] = combs
    
        print(combs)
    return combs, known

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

def parse_data(row: str, mode: int):
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

if __name__ == '__main__':
    main()