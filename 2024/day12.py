data = open("input_dayc.txt").read().splitlines()
visited = {}
R,C = len(data), len(data[0])

def get_regions():
    regions = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i,j) in visited: continue
            regions.append(search_neighbours(i,j,[],data[i][j]))
    return regions

def search_neighbours(i,j,neigbours,char):
    # Recursive approach for finding the regions

    if (i,j) in visited: return neigbours
    else: visited[(i,j)] = 1
    neigbours.append((i,j))

    if i > 0:
        if data[i-1][j] == char:
            neigbours = search_neighbours(i-1,j,neigbours,char)
    if i < R-1:
        if data[i+1][j] == char:
            neigbours = search_neighbours(i+1,j,neigbours,char)
    if j > 0:
        if data[i][j-1] == char:
            neigbours = search_neighbours(i,j-1,neigbours,char)
    if j < C-1:
        if data[i][j+1] == char:
            neigbours = search_neighbours(i,j+1,neigbours,char)
    return neigbours

def get_perimeter(region):
    # Pretty straight forward, if a node next to the region node 
    # is not in region, increase perimeter size
    p = 0
    for node in region:
        if (node[0]-1,node[1]) not in region: p += 1
        if (node[0]+1,node[1]) not in region: p += 1
        if (node[0],node[1]-1) not in region: p += 1
        if (node[0],node[1]+1) not in region: p += 1
    return p

def get_sides(region):
    s = 0

    # Get all nodes that are touching the region
    snodes = []
    for node in region:
        if (node[0]-1,node[1]) not in region: snodes.append((node[0]-1, node[1]))
        if (node[0]+1,node[1]) not in region: snodes.append((node[0]+1, node[1]))
        if (node[0],node[1]-1) not in region: snodes.append((node[0], node[1]-1))
        if (node[0],node[1]+1) not in region: snodes.append((node[0], node[1]+1))
    snodes = list(set(snodes))

    # Process each neighbour node
    for node in snodes:
        # Checking each side of the neighbour node if the initialize a side of the region based on 
        # predefined rules
        
        i,j = node[0],node[1]

        # Left side
        if (i,j-1) in region:
            if (i-1,j) in region and (i+1,j) in region: s += 1 # region node on both sides -> side
            elif (i-1,j-1) not in region and (i+1,j-1) not in region: s += 1 # no other region nodes above/below the region node -> side
            elif (i-1,j-1) not in region: s += 1 # no other region node above the region node -> side (rule for processing long sides)
            elif (i-1,j) in region: s+=1 # region node above the neighbour node -> side (another rule)

        # Similar rules apply for next sides

        # Right side
        if (i,j+1) in region:
            if (i-1,j) in region and (i+1,j) in region: s += 1 
            elif (i-1,j+1) not in region and (i+1,j+1) not in region: s += 1 
            elif (i-1,j+1) not in region: s += 1 
            elif (i-1,j) in region: s+=1 

        # Upside
        if (i-1,j) in region:
            if (i,j-1) in region and (i,j+1) in region: s += 1 
            elif (i-1,j+1) not in region and (i-1,j-1) not in region: s += 1
            elif (i-1,j+1) not in region: s += 1
            elif (i,j+1) in region: s += 1

        # Downside
        if (i+1,j) in region:
            if (i,j-1) in region and (i,j+1) in region: s += 1
            elif (i+1,j+1) not in region and (i+1,j-1) not in region: s += 1 
            elif (i+1,j+1) not in region: s += 1
            elif (i,j+1) in region: s += 1

    return s

regions = get_regions()
silver, gold = 0, 0
for r in regions:
    silver += len(r)*get_perimeter(r)
    gold += len(r)*get_sides(r)
print("Silver:", silver)
print("Gold:", gold)
