def main():
    fname = '2015/day01/input.txt'
    file = open(fname, 'r')
    data = file.readline()
    # Finding the end level by counting the difference
    print("Part 1:", data.count('(') - data.count(')'))
    # Finding the first state when basement was reached
    floor = 0
    for i,c in enumerate(data):
        # Updating the current floor
        if c == '(': floor += 1
        else: floor -= 1
        # If basement is reached, end the loop
        if floor < 0:
            print("Part 2:", i+1)
            break


if __name__ == '__main__':
    main()