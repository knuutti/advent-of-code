def main():

    fname = "d2_data.txt"
    file = open(fname, 'r')
    content = file.readlines()

    depth = 0
    pos = 0
    aim = 0

    for row in content:
        temp = row.split(" ")
        
        if temp[0] == "forward":
            pos += int(temp[1].rstrip("\n"))
            depth += aim*int(temp[1].rstrip("\n"))
        elif temp[0] == "up":
            aim -= int(temp[1].rstrip("\n"))
        else:
            aim += int(temp[1].rstrip("\n"))

    print(f"Part 1: {pos*aim}")
    print(f"Part 2: {pos*depth}")

if __name__ == "__main__":
    main()






    