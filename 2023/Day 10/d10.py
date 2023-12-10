import time

def main():   
    fname = "./2023/Day 10/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    start = find_start_index(data)
    pipes = find_connectives(start,data,[0,0])

    #print(start, pipes)
    
    counter = 1
    current_pipe = pipes[0]
    delta = [current_pipe[0]-start[0],current_pipe[1]-start[1]]

    while current_pipe != start:
        #time.sleep(0.5)
        new_pipe = find_connectives(current_pipe,data,delta)[0]
        delta = [new_pipe[0]-current_pipe[0],new_pipe[1]-current_pipe[1]]
        current_pipe = new_pipe
        print(current_pipe, data[current_pipe[0]][current_pipe[1]])
        counter += 1

    print(counter//2)

def find_start_index(data):
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "S":
                return [r,c]

def find_connectives(start,data,delta):
    pipes = []
    curr = data[start[0]][start[1]]
    if start[1] != 0 and delta[1] != 1 and curr not in ["F","L", "|"]:
        pipe_west = data[start[0]][start[1]-1]
        if pipe_west in ["-", "L", "F", "S"]:
            pipes.append([start[0], start[1]-1])
    if start[1] != len(data[0])-1 and delta[1] != -1 and curr not in ["J","7", "|"]:
        pipe_east = data[start[0]][start[1]+1]
        if pipe_east in ["-", "J", "7", "S"]:
            pipes.append([start[0], start[1]+1])
    if start[0] != 0 and delta[0] != 1 and curr not in ["-","F", "7"]:
        pipe_north = data[start[0]-1][start[1]]
        if pipe_north in ["|", "F", "7", "S"]:
            pipes.append([start[0]-1, start[1]])
    if start[0] != len(data)-1 and delta[0] != -1 and curr not in ["J","L", "-"]:
        pipe_south = data[start[0]+1][start[1]]
        if pipe_south in ["|", "J", "L", "S"]:
            pipes.append([start[0]+1, start[1]])
    return pipes


if __name__ == "__main__":
    main()