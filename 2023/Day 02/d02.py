# Advent of Code 2023 - Day 2
# Eetu Knutars / @knuutti

def main():   
    
    fname = "./2023/Day 02/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    file.close()

    cube_limits = {"red": 12, "green": 13, "blue": 14}

    sum_of_ids = 0
    sum_of_powers = 0

    for line in data:
        result = analyse(line, cube_limits)
        sum_of_ids += result[0]
        sum_of_powers += result[1]

    print("Part 1:", sum_of_ids)
    print("Part 2:", sum_of_powers)

# Analysing one line of the input
def analyse(line, cube_limits):

    temp = line.split(": ")
    id = int(temp[0].lstrip("Game "))
    sets = temp[1].split("; ")
    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for game_set in sets:

        amounts = {"red": 0, "green": 0, "blue": 0}
        cubes = game_set.split(", ")

        for cube in cubes:
            # Update the amount of cubes in the set
            cube = cube.split(" ")
            amounts[cube[1]] += int(cube[0])

        for color in amounts:
            # If current amount of one color is more than the previous minimum -> update the value
            if amounts[color] > min_cubes[color]:
                min_cubes[color] = amounts[color]

    # Calculating the power from the required cubes
    total = 1
    for color in min_cubes:
        if min_cubes[color] > cube_limits[color]:
            id = 0 # If minimum cubes is more than the limit, don't add anything to sum of IDs
        total *= min_cubes[color]

    return [id, total]



if __name__ == "__main__":
    main()