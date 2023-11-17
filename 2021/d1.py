def main():

    fname = "d1_data.txt"
    file = open(fname, 'r')
    content = file.readlines()
    cur_depth = int(content[0].rstrip('\n'))
    content.pop(0)
    counter = 0
    windows_counter = 0

    prev = [cur_depth]

    for i,row in enumerate(content):
        new_depth = int(row.rstrip('\n'))

        # Part 1 increment
        if new_depth > cur_depth:
            counter += 1

        # Part 2 increment (3 tile window)
        prev.append(new_depth)
        if len(prev) == 4:
            if sum(prev[0:3]) < sum(prev[1:]):
                windows_counter += 1
            prev.pop(0)

        cur_depth = new_depth

    print(f"Part 1: {counter}")
    print(f"Part 2: {windows_counter}")

if __name__ == "__main__":
    main()






    