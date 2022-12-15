#   Advent of Code 2022 - Day 15
#   Eetu Knutars / @knuutti

def main():
    
    file_name = 'D15_data.txt'
    file = open(file_name, 'r')
    data = file.read().splitlines()
    file.close()

    LEVEL = 2000000

    impossible_positions = {}

    for line in data:
        line = line.split(', ')
        sensor_x = int(line[0].lstrip('Sensor at x='))
        beacon_y = int(line[2].lstrip('y='))
        line = line[1].split(': closest beacon is at x=')
        sensor_y = int(line[0].lstrip('y='))
        beacon_x = int(line[1])

        distance = abs(sensor_x-beacon_x)+abs(sensor_y-beacon_y)

        for x_distance in range(distance + 1):
            y_distance_max = distance - x_distance

            if abs(LEVEL-sensor_y) <= y_distance_max:
                impossible_positions[(sensor_x - x_distance, LEVEL)] = 0
                impossible_positions[(sensor_x + x_distance, LEVEL)] = 0

        if (beacon_x, beacon_y) in impossible_positions:
            del impossible_positions[(beacon_x, beacon_y)]

    print("Part 1:", len(impossible_positions))




if __name__ == '__main__':
    main()