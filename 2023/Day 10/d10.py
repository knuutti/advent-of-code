# Advent of Code 2023 - Day 10
# Eetu Knutars / @knuutti

# Slightly more complicated than the previous day

def main():   
    fname = "./2023/Day 10/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    start = find_start_index(data)
    start_type = get_start_type(start, data)
    pipes = find_connectives(start,data,[0,0])
    
    counter = 1
    current_pipe = pipes
    delta = [current_pipe[0]-start[0],current_pipe[1]-start[1]]

    total_pipes = {str(start): start_type}
    data[start[0]] = data[start[0]].replace("S", start_type)

    min_y = start[0]
    max_y = start[0]
    min_x = start[1]
    max_x = start[1]

    while current_pipe != start:

        if current_pipe[0] < min_y: min_y = current_pipe[0]
        if current_pipe[0] > max_y: max_y = current_pipe[0]
        if current_pipe[1] < min_x: min_x = current_pipe[1]
        if current_pipe[1] > max_x: max_x = current_pipe[1]

        total_pipes[str(current_pipe)] = data[current_pipe[0]][current_pipe[1]]
        new_pipe = find_connectives(current_pipe,data,delta)
        delta = [new_pipe[0]-current_pipe[0],new_pipe[1]-current_pipe[1]]
        current_pipe = new_pipe
        counter += 1


    # Finding the bits withing the loop
    withins = {}
    previous_corner = None
    for i in range(min_y, max_y+1):
        vertical_pipe_counter = 0
        for j in range(min_x, max_x+1):
            if str([i,j]) in total_pipes and data[i][j] == "|":
                vertical_pipe_counter += 1
                continue
            elif str([i,j]) not in total_pipes and vertical_pipe_counter % 2 == 1:
                withins[str([i,j])] = 1
            elif str([i,j]) in total_pipes and data[i][j] != "-": # dealing with corners
                if not previous_corner:
                    previous_corner = data[i][j]
                else:
                    a = 0
                    if previous_corner == "F": a+=0.5
                    elif previous_corner == "L": a-=0.5
                    if data[i][j] == "J": a+=0.5
                    elif data[i][j] == "7": a-=0.5
                    previous_corner = None
                    if a:
                        vertical_pipe_counter += 1
    
    print("Part 1:", counter//2)
    print("Part 2:", len(withins))



def find_start_index(data):
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "S":
                return [r,c]

def get_start_type(start,data):
    v,h = 0,0
    if start[1] != 0:
        pipe_west = data[start[0]][start[1]-1]
        if pipe_west in ["-", "L", "F"]:
            h = -1
    if start[1] != len(data[0])-1:
        pipe_east = data[start[0]][start[1]+1]
        if pipe_east in ["-", "J", "7"]:
            h = 1
    if start[0] != 0:
        pipe_north = data[start[0]-1][start[1]]
        if pipe_north in ["|", "F", "7"]:
            v = -1
    if start[0] != len(data)-1:
        pipe_south = data[start[0]+1][start[1]]
        if pipe_south in ["|", "J", "L"]:
           v = 1

    if not v:
        return "-"
    elif not h:
        return "|"
    elif v == -1 and h == -1:
        return "J"
    elif v == 1 and h == -1:
        return "7"
    elif v == -1 and h == 1:
        return "L"
    else:
        return "F"



def find_connectives(start,data,delta):
    curr = data[start[0]][start[1]]
    if start[1] != 0 and delta[1] != 1 and curr not in ["F","L", "|"]:
        pipe_west = data[start[0]][start[1]-1]
        if pipe_west in ["-", "L", "F", "S"]:
            return [start[0], start[1]-1]
    if start[1] != len(data[0])-1 and delta[1] != -1 and curr not in ["J","7", "|"]:
        pipe_east = data[start[0]][start[1]+1]
        if pipe_east in ["-", "J", "7", "S"]:
            return [start[0], start[1]+1]
    if start[0] != 0 and delta[0] != 1 and curr not in ["-","F", "7"]:
        pipe_north = data[start[0]-1][start[1]]
        if pipe_north in ["|", "F", "7", "S"]:
            return [start[0]-1, start[1]]
    if start[0] != len(data)-1 and delta[0] != -1 and curr not in ["J","L", "-"]:
        pipe_south = data[start[0]+1][start[1]]
        if pipe_south in ["|", "J", "L", "S"]:
           return [start[0]+1, start[1]]


if __name__ == "__main__":
    main()