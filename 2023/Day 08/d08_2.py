# Advent of Code 2023 - Day 8
# Eetu Knutars / @knuutti

import math

def main():   
    fname = "./2023/Day 08/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    instructions = data[0]
    instructions = list(map(lambda x: int(x), instructions.replace("L", "0").replace("R", "1"))) 

    print("Part 1:", analyse(data,instructions,0))
    print("Part 2:", analyse(data,instructions,1))
    
# Returns the required steps to achieve the goal
def analyse(data, instructions, mode):
    # Defining the directions for each node as well as the start nodes
    current_nodes = []
    directions = {}
    for row in data[2:]:
        row = row.split()
        start = row[0][0:4]
        left = row[2][1:4]
        right = row[3][0:3]
        directions[start] = [left, right]
        if (row[0][2] == "A" and mode == 1) or row[0] == "AAA":
            current_nodes.append(start)

    # Examining the loop structures
    total_z = []
    for start_node in current_nodes:
        node = start_node
        i = 1 # tracks the instruction index
        counter = 0 # tracks the entire loop length
        z_locations = [] # tracks the Z-ending values in the loop
        d = {start_node: {1:0}} # storing each node to dictionary with additional information
        while True:
            counter += 1
            node = directions[node][instructions[i-1]] # update the node
            if (node[2] == "Z" and mode == 1) or node == "ZZZ": # possible end point is found
                z_locations.append(counter) 
            i += 1
            if i == len(instructions):
                i = 0

            if node not in d: # never visited the node
                d[node] = {i:counter}
            elif i not in d[node]: # never visited the node with current instruction index
                d[node][i] = counter
            else: # second visit with same instruction index
                total_z.extend(z_locations)
                break

    return lcm(total_z)

# Function for calculating least common multiple from a list of integers
def lcm(numbers: list):
    x = 1
    for i in numbers:
        x = x*i//math.gcd(x, i)
    return x



if __name__ == "__main__":
    main()