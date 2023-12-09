def main():   
    fname = "./2023/Day 09/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    silver = 0
    gold = 0
    for row in data:
        row = [int(x) for x in row.split()]
        next = recursive_thing(row, 0)
        prev = recursive_thing(row, 1)
        silver += next
        gold += prev

    print("Part 1:", silver)
    print("Part 2:", gold)


def recursive_thing(line, mode):
    if sum(line) == 0:
        return 0
    else:
        diffs = [line[i+1-mode]-line[i+mode] for i in range(0,len(line)-1)]
        return line[-1+mode] + recursive_thing(diffs, mode)


if __name__ == "__main__":
    main()