# Advent of Code 2022 - Day 9
# Eetu Knutars / @knuutti

def main():

    file_name = "D9_data.txt"
    file = open(file_name, 'r')
    data = file.read().splitlines()

    # Storing the current coordinates of each knot into a list
    # Starting position is the origin
    knots = [[0,0] * 1 for _ in range(10)]

    # Defining the dictionaries for storing the visited coordinates
    visited_1, visited_9 = {(0,0): 0}, {(0,0): 0}

    for operation in data:
        
        temp = operation.split()
        direction = temp[0]
        length = int(temp[1])

        for _ in range(length):
            
            if direction == "R":
                knots[0][0] += 1
            elif direction == "U":
                knots[0][1] += 1
            elif direction == "L":
                knots[0][0] -= 1
            else:
                knots[0][1] -= 1

            for i in range(1, 10):
                head = knots[i-1]
                tail = knots[i]

                if (head[0] - tail[0]) ** 2 < 4 and (head[1] - tail[1]) ** 2 < 4:
                    # No empty space between tail and head -> no need to move
                    continue

                elif (head[0] - tail[0]) ** 2 == 4 and (head[1] - tail[1]) ** 2 == 4:
                    # Tail should be placed diagonally in relation to the head
                    if head[0] > tail[0]:
                        tail[0] = head[0] - 1
                    else:
                        tail[0] = head[0] + 1

                    if head[1] > tail[1]:
                        tail[1] = head[1] - 1
                    else:
                        tail[1] = head[1] + 1

                else:
                    # Tail should be placed behind the head
                    if (head[0] - tail[0]) ** 2 == 4:
                        # There is empty space in X-axis
                        if head[0] > tail[0]:
                            tail[0] = head[0] - 1
                        else:
                            tail[0] = head[0] + 1

                        tail[1] = head[1]

                    else:
                        # There is empty space in Y-axis
                        if head[1] > tail[1]:
                            tail[1] = head[1] - 1
                        else:
                            tail[1] = head[1] + 1

                        tail[0] = head[0]

                # Updating the visited coordinates

                if i == 1:
                    # Part 1
                    if (tail[0], tail[1]) not in visited_1:
                            visited_1[(tail[0], tail[1])] = 0

                elif i == 9:
                    # Part 2
                    if (tail[0], tail[1]) not in visited_9:
                            visited_9[(tail[0], tail[1])] = 0

    print("Part 1:", len(visited_1))
    print("Part 2:", len(visited_9))

if __name__ == "__main__":
    main()
