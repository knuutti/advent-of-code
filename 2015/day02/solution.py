def main():
    fname = '2015/day02/example.txt'
    file = open(fname, 'r')
    data = file.read().splitlines()
    paper,ribbon = 0,0
    for row in data:
        # Finding the side lengths and sorting them
        sides = sorted([int(x) for x in row.split('x')])
        # Updating the paper value
        paper += 3*sides[0]*sides[1] + 2*(sides[0]*sides[2] + sides[1]*sides[2])
        # Updating the ribbon value
        ribbon += 2*(sides[0]+sides[1]) + sides[0]*sides[1]*sides[2]
    print("Part 1:",paper)
    print("Part 2",ribbon)


if __name__ == '__main__':
    main()