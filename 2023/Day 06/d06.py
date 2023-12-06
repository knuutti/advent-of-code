# Advent of Code 2023 - Day 6
# Eetu Knutars / @knuutti

# Math is always the solution (at least for optimizing)

from math import sqrt,ceil,floor,prod

def main():   
    fname = "./2023/Day 06/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    # Gets a list of times and distance (overcomplicated)
    times, distances = [map(lambda y: int(y),x) for x in [row.split(":")[1].split() for row in data]]
    print("Part 1:", prod(map(analyse, times, distances)))
    # Combines the numbers as one
    time, distance = [int("".join(line.split(":")[1].split())) for line in data]
    print("Part 2:", analyse(time,distance))

def analyse(time,distance):
    # Using the general formula for solving quadratic equation
    b = -time
    c = distance
    s = ceil(0.5*(-b-sqrt((b**2)-(4*c))))
    e = floor(0.5*(-b+sqrt((b**2)-(4*c))))
    # Bypassing the edge cases
    if distance - time*(s) + (s)**2 > 0: s+= 1
    if distance - time*(e) + (e)**2 > 0: e-= 1
    return e-s+1

if __name__ == "__main__":
    main()