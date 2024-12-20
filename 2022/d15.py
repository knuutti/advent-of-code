#   Advent of Code 2022 - Day 15
#   Eetu Knutars / @knuutti

#   Runtime is something else... but it works :D

def main():
    
    file_name = 'd15_data.txt'
    file = open(file_name, 'r')
    data = file.read().splitlines()
    file.close()

    LEVEL = 2000000
    LIMIT = 4000000

    impossible_positions = {}
    sensors = {}

    for line in data:
        line = line.split(', ')
        sensor_x = int(line[0].lstrip('Sensor at x='))
        beacon_y = int(line[2].lstrip('y='))
        line = line[1].split(': closest beacon is at x=')
        sensor_y = int(line[0].lstrip('y='))
        beacon_x = int(line[1])
        distance = abs(sensor_x-beacon_x)+abs(sensor_y-beacon_y)
        sensors[(sensor_x,sensor_y)] = distance

        for x_distance in range(distance + 1):
            y_distance_max = distance - x_distance

            if abs(LEVEL-sensor_y) <= y_distance_max:
                impossible_positions[(sensor_x - x_distance, LEVEL)] = 0
                impossible_positions[(sensor_x + x_distance, LEVEL)] = 0

        if (beacon_x, beacon_y) in impossible_positions:
            del impossible_positions[(beacon_x, beacon_y)]

    print("Part 1:", len(impossible_positions))

    # Part 2
    for sensor1 in sensors:
        sensor_edges = area_edges(sensor1[0],sensor1[1],sensors[sensor1])
        selected_point = None
        for point in sensor_edges:
            if point[0] < 0 or point[0] > LIMIT or point[1] < 0 or point[1] > LIMIT: # if point is off the grid
                continue
            selected_point = point
            for sensor2 in sensors:
                if sensor1 == sensor2: # dont check the current sensor
                    continue
                if is_inside_radius(point[0],point[1],sensor2[0],sensor2[1],sensors[sensor2]): # if inside sensors radius
                    selected_point = None
                    break

            if selected_point:
                break

        if selected_point:
            break

    print("Part 2:", 4000000*selected_point[0]+selected_point[1])
        

def area_edges(x,y,radius):
    edges = [(x-radius-1, y), (x+radius+1, y), (x,y+radius+1), (x,y-radius-1)]

    for i in range(1,radius+1):
        edges.append((x-i,y+(radius-i+1)))
        edges.append((x-i,y-(radius-i+1)))
        edges.append((x+i,y+(radius-i+1)))
        edges.append((x+i,y-(radius-i+1)))

    return edges

def is_inside_radius(point_x,point_y,sensor_x,sensor_y,sensor_radius):
    return abs(point_x-sensor_x)+abs(point_y-sensor_y) <= sensor_radius



if __name__ == '__main__':
    main()