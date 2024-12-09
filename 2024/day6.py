data = open("input_day6.txt",'r').read().splitlines()

obstacles = {}
direction = -1
visited = {}
ROWS, COLUMNS = len(data), len(data[0])
for i in range(ROWS):
    for j in range(COLUMNS):
        if data[i][j] == "#":
            obstacles[(i,j)] = 1
        elif direction == -1:
            if data[i][j] == "^": direction = 1
            elif data[i][j] == "v": direction = 3
            elif data[i][j] == "<": direction = 0
            elif data[i][j] == ">": direction = 2
            else: continue
            start = (i,j)
            visited[start] = 1
start_direction = direction
curr = start
while True:
    i,j = curr[0], curr[1]

    # End of map reached -> end
    if direction == 1 and i == 0: break
    if direction == 2 and j == COLUMNS-1: break
    if direction == 3 and i == ROWS - 1: break
    if direction == 4 and j == 0: break

    # Obstacle in way -> turn
    if direction == 1 and (i-1,j) in obstacles: direction = (direction+1)%4
    elif direction == 2 and (i,j+1) in obstacles: direction = (direction+1)%4
    elif direction == 3 and (i+1,j) in obstacles: direction = (direction+1)%4
    elif direction == 0 and (i,j-1) in obstacles: direction = (direction+1)%4

    else:
        if direction == 0: curr = (i,j-1)
        elif direction == 1: curr = (i-1,j)
        elif direction == 2: curr = (i,j+1)
        elif direction == 3: curr = (i+1,j)
    visited[curr] = 1

print("Silver:", len(visited))



gold = 0
for node in visited:
    if node == start: continue
    obstacles[node] = 1
    curr = start
    direction = start_direction
    visited_directions = {}
    visited_directions[(start[0], start[1], direction)] = 1
    
    #print(node)
    while True:
        i,j = curr[0], curr[1]

        # End of map reached -> end
        if direction == 1 and i == 0: break
        if direction == 2 and j == COLUMNS-1: break
        if direction == 3 and i == ROWS - 1: break
        if direction == 0 and j == 0: break

        # Obstacle in way -> turn
        if direction == 1 and (i-1,j) in obstacles: direction = (direction+1)%4
        elif direction == 2 and (i,j+1) in obstacles: direction = (direction+1)%4
        elif direction == 3 and (i+1,j) in obstacles: direction = (direction+1)%4
        elif direction == 0 and (i,j-1) in obstacles: direction = (direction+1)%4

        else:
            if direction == 0: curr = (i,j-1)
            elif direction == 1: curr = (i-1,j)
            elif direction == 2: curr = (i,j+1)
            elif direction == 3: curr = (i+1,j)
        
        if (curr[0], curr[1], direction) in visited_directions:
            gold += 1
            break
        visited_directions[(curr[0], curr[1], direction)] = 1


    del obstacles[node]

print("Gold:", gold)