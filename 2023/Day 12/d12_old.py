import itertools

def main():   
    fname = "./2023/Day 12/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    counter = 0
    for row in data:
        conditions, groups = parse_data(row)
        counter += analyse(conditions, groups)
    print(counter)

def analyse(conditions: str, groups):
    combinations = 0
    test_condinations = ""
    unknown_indeces = []
    for i in range(len(conditions)):
        if conditions[i] == "?":
            unknown_indeces.append(i)
            test_condinations += "."
        else:
            test_condinations += conditions[i]
    
    r = sum(groups) - test_condinations.count("#")
    if r>0:
        unknown_combinations = list(itertools.combinations(unknown_indeces, r))
        for x in unknown_combinations:
            row = test_condinations
            for y in x:
                row = row[:y] + "#" + row[y+1:]
            broken = row.replace(".", " ").split()
            lens = [len(x) for x in broken]
            if lens == groups:
                combinations += 1

    # Testing with no extra broken parts
    broken = test_condinations.replace(".", " ").split()
    lens = [len(x) for x in broken]
    if lens == groups:
        combinations += 1
    #print(combinations)
    return combinations


def parse_data(data):
    data = data.split()
    conditions = data[0]# + 4*("?"+data[0])
    #print(conditions)
    groups = [int(x) for x in data[1].split(",")]
    for i in range(0):
        groups.extend([int(x) for x in data[1].split(",")])
    return conditions, groups


if __name__ == "__main__":
    main()