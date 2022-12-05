# Advent of Code 2022 - Day 5
# Eetu Knutars / @knuutti

import sys
import time

def analyse(file_name, mode):

    data_file = open(file_name, "r")
    data = data_file.readlines()

    # Finding the amount of piles
    for row in data:
        if row[1] != "1":
            continue
        else:
            piles = row.rstrip().split(" ")
            N = int(piles[len(piles)-1])    # storing the amount of piles
            break
                

    # Storing the crate data in a matrix
    stacks = [[] * i for i in range(N)]

    # Looping through the starting positions
    for i,row in enumerate(data):

        # Breaking the loop once the instructions start
        if row[1] == "1":
            operation_start = i + 2
            break
        
        for i in range(1, N*4, 4):
            if row[i] != " ":
                stacks[(i-1)//4].append(row[i])

    
    # Looping through the instructions
    for row in data[operation_start:]:

        if len(row) == 0:
            break

        # Parsing the data
        temp = row.split(" ")
        #print(temp)
        amount = int(temp[1])
        start = int(temp[3])-1
        end = int(temp[5])-1

        # Doing the crate operation
        for i in range(amount):
            if mode.lower() == "n":
                stacks[end].insert(0,stacks[start][0])
            else:
                stacks[end].insert(i,stacks[start][0])
            stacks[start].pop(0)

    return stacks

if __name__ == "__main__":

    file_name = input("Give file name to read: ")
    mode = input("Can the crane lift multiple crates? (y/n): ")
    print()
    if mode.lower() == "y":
        crane = 1
    elif mode.lower() == "n":
        crane = 0
    else:
        print("I asked for yes or no, not that hard...")
        sys.exit()

    start = time.time()

    stacks = analyse(file_name, mode)
    for stack in stacks:
        print(stack[0], end="")

    end = time.time()

    print(f"\n\nRunning time: {end-start:.2f}s")
