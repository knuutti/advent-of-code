#   Advent of Code 2022 - Day 10
#   Eetu Knutars / @knuutti

def main():

    signals = [20, 60, 100, 140, 180, 220]
    line_breaks = [40, 80, 120, 160, 200]
    signal_strengths = [0, 0, 0, 0, 0, 0]
    sprite_position = [0, 1, 2]
    sprite = ""

    file_name = "d10_data.txt"
    file = open(file_name, 'r')
    data = file.read().splitlines()
    file.close()

    x = 1
    cycle = 0

    for line in data:
        units = line.split()

        if units[0] == "noop":
            cycle_number = 1
        else:
            cycle_number = 2

        for _ in range(cycle_number):

            if cycle in line_breaks:
                # In case we should break the line, update x value and sprite position
                sprite += "\n"
                x += 40
                sprite_position = [x-1, x, x+1]

            # Drawing based on the sprite position
            if cycle in sprite_position:
                sprite += "#"
            else:
                # I replaced "." with an empty space to make the image more readable
                sprite += " "

            cycle += 1
            if cycle in signals:
                # Update the signal strengths
                signal_strengths[signals.index(cycle)] = x * cycle

        if cycle_number == 2:
            # If the command was "addx", change x value
            x += int(units[1])

        # Update the sprite position at the end of each cycle
        sprite_position = [x-1, x, x+1]

    print("Part 1:", sum(signal_strengths))
    print("Part 2:\n", sprite) # results in BGKAEREZ with my input data

if __name__ == "__main__":
    main()


