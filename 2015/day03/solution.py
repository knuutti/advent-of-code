def main():
    fname = '2015/day03/input.txt'
    file = open(fname, 'r')
    data = file.readline()
    print("Part 1:",silver(data))
    print("Part 2:",gold(data))

# Solution to part one
def silver(data):
    locs = {(0,0): 1}
    x,y = 0,0
    for symbol in data:
        # Change the location
        if symbol == '>': x+=1
        elif symbol == '<': x-=1
        elif symbol == 'v': y-=1
        else: y+=1
        # Add house to the set if not visited
        if (x,y) not in locs: locs[(x,y)] = 0
    return len(locs)

# Solution to part two
def gold(data):
    locs = {(0,0): 1}
    sx,sy,rx,ry = 0,0,0,0
    for i,symbol in enumerate(data):
        # Check which Santa is going to move
        x = sx if i%2 == 0 else rx
        y = sy if i%2 == 0 else ry
        # Change the location
        if symbol == '>': x+=1
        elif symbol == '<': x-=1
        elif symbol == 'v': y-=1
        else: y+=1
        # See if the house is visited already (if not, add to the set)
        if (x,y) not in locs: locs[(x,y)] = 0
        # Update the location for the next iteration
        if i % 2 == 0: sx,sy = x,y
        else: rx,ry = x,y
    return len(locs)


if __name__ == '__main__':
    main()