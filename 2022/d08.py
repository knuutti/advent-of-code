# Advent of Code 2022 - Day 8
# Eetu Knutars / @knuutti

def main():

    data_file = open("d08_data.txt", 'r')
    data = data_file.read().splitlines()

    # Defining the row and column lengths
    rows = len(data)
    columns = len(data[0])

    # Storing the data into a matrix as integer values
    M = []
    for i in range(0, rows):
        M.append([])
        for j in range(0, columns):
            M[i].append(int(data[i][j]))


    # Part 1: Computing the number of visible treese
    total = 0
    for i in range(1, rows-1):
        for j in range(1, columns-1):

            # Variables for tracking the max heights for each direction
            up_max, down_max, left_max, right_max = 0,0,0,0

            for k in range(i+1,rows):
                # South
                if M[k][j] > down_max:
                    down_max = M[k][j]
            for k in range(0, i):
                # North
                if M[k][j] > up_max:
                    up_max = M[k][j]
            for k in range(j+1, columns):
                # East
                if M[i][k] > right_max:
                    right_max = M[i][k]
            for k in range(0, j):
                # West
                if M[i][k] > left_max:
                    left_max = M[i][k]

            # If tree height is higher than any of the max heights, tree is visible
            if M[i][j] > min(up_max, down_max, left_max, right_max):
                total += 1

    # Adding the number of edge trees to the total sum
    total += 2*rows + 2*(columns-2)

    print("Part 1:", total)

    # Part 2: Finding the best scenic score
    max = 0
    for i in range(1, rows-1):
        for j in range(1, columns-1):

            # Defining the direction scores as zeros
            scores = [0,0,0,0]

            for k in range(i+1,rows):
                # South
                scores[0] += 1
                if M[k][j] >= M[i][j]:
                    break

            for k in range(i-1, -1, -1):
                # North
                scores[1] += 1
                if M[k][j] >= M[i][j]:
                    break

            for k in range(j+1, columns):
                # East
                scores[2] += 1
                if M[i][k] >= M[i][j]:
                    break

            for k in range(j-1, -1, -1):
                # West
                scores[3] += 1
                if M[i][k] >= M[i][j]:
                    break

            # Computing the total score for a tree
            tree_max = scores[0]*scores[1]*scores[2]*scores[3]
            if tree_max > max:
                # Score is higher than max value -> update max value
                max = tree_max

    print("Part 2:", max)

if __name__ == "__main__":
    main()