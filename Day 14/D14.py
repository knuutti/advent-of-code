#   Advent of Code 2022 - Day 14
#   Eetu Knutars / @knuutti

def main():

    # Reading the data
    file_name = "D14_data.txt"
    file = open(file_name, 'r')
    data = file.read().splitlines()

    full_block = {}
    max_y = 0
    part_1_result = None

    # Storing the data into a data structure
    coordinates = []
    for i,line in enumerate(data):
        coordinates.append([])
        points = line.split(" -> ")
        for point in points:
            temp = point.split(",")
            coordinates[i].append([int(temp[0]), int(temp[1])])

    for path in coordinates:
        for point in path:
            if point[1] > max_y:
                max_y = point[1]
        for i in range(len(path) - 1):
            if path[i][0] == path[i+1][0]:
                # X-coordinate is constant
                if path[i][1] < path[i+1][1]:
                    for j in range(path[i][1], path[i+1][1] + 1):
                        full_block[(path[i][0]), j] = 0
                else:
                    for j in range(path[i+1][1], path[i][1] + 1):
                        full_block[(path[i][0]), j] = 0
            else:
                # Y-coordinate is constant
                if path[i][0] < path[i+1][0]:
                    for j in range(path[i][0], path[i+1][0] + 1):
                        full_block[j, (path[i][1])] = 0
                else:
                    for j in range(path[i+1][0], path[i][0] + 1):
                        full_block[j, (path[i][1])] = 0

    # Y-level of the infinite floor
    max_y += 2

    # Adding the "infinite" floor
    for i in range(500-200, 500+200):
        full_block[(i, max_y)] = 0

    # Starting condition
    sand_amount = 0
    sand_location = [500, 0]

    while True:

        # If the source is blocked, break the loop
        if (sand_location[0], sand_location[1]) in full_block:
            break

        # If the sand flows over the floor, 
        # store the sand amount (Part 1 result)
        if sand_location[1] > max_y-2 and not part_1_result:
            part_1_result = sand_amount
            print("Part 1:", part_1_result)
            continue
        

        if (sand_location[0], sand_location[1]+1) in full_block:
            # Block below is blocked

            if (sand_location[0]-1, sand_location[1]+1) in full_block:
                # Block in down left is blocked

                if (sand_location[0]+1, sand_location[1]+1) in full_block:
                    # Block in down right is blocked -> sand is settled

                    # Increase the sand value, add the coordinates 
                    # as full block and continue to the next iteration
                    sand_amount += 1
                    full_block[(sand_location[0], sand_location[1])] = 0
                    sand_location = [500, 0]
                    continue

                else:
                    # Move sand to down right
                    sand_location = [sand_location[0]+1, sand_location[1]+1]
            else:
                # Move sand to down left
                sand_location = [sand_location[0]-1, sand_location[1]+1]
        else:
            # Move sand directly down
            sand_location = [sand_location[0], sand_location[1]+1]

    # Final sand count when the source is blocked
    print("Part 2:", sand_amount)

if __name__ == "__main__":
    main()
