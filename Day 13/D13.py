#   Advent of Code 2022 - Day 13
#   Eetu Knutars / @knuutti

import json

def main():

    # Reading the data
    file_name = "D13_data.txt"
    file = open(file_name, 'r')
    data = file.read().splitlines()
    file.close()

    # Converting strings to data types using json-library
    i, M = 0, [[]]
    for packet in data:
        if len(packet) == 0:
            i += 1
            M.append([])
            continue
        M[i].append(json.loads(packet))

    score = 0
    for i,pair in enumerate(M):

        order = compare(pair[0], pair[1])
        if order >= 0:
            # If the pair is in order, increase the score
            score += i+1

    print("Part 1:", score)
    
    # List for storing the items in order
    sorted_list = []

    for i,pair in enumerate(M):
        for i in range(2):
            # Inserting both item from the pair 
            # to the sorted list
            order = -1
            for j,item in enumerate(sorted_list):
                order = compare(pair[i], item)
                if order >= 0:
                    # The current item in sorted list is 
                    # greater than the prosessed item
                    # -> put the item here
                    sorted_list.insert(j, pair[i])
                    break
            if order < 0:
                # If the item should be put 
                # to the end of the list
                sorted_list.append(pair[i])

    # Now we need to find the locations of 
    # [[2]] and [[6]] in the sorted list
    loc = [0,0]
    dividers = [[[2]],[[6]]]

    for j,divider in enumerate(dividers):
        # Finding the location of the dividers
        for i,item in enumerate(sorted_list):
                order = compare(divider, item)
                if order >= 0:
                    # Location of the divider
                    loc[j] = i + j + 1
                    break

    print("Part 2:", loc[0]*loc[1])
    
# Function for comparing two items
def compare(left, right):

    order = 0

    # If either one of the values is integer 
    # while the other one is a list
    if type(left) is int and type(right) is not int:
            left = [left]
    elif type(right) is int and type(left) is not int:
            right = [right]

    # Both values are integers -> calculate the difference
    if type(left) is int:
        order = right - left
    
    # Both values are lists -> process them
    else:

        # If either one or both of the lists are empty
        if len(right) == 0 and len(left) > 0:
            order = -1
        elif len(left) == 0 and len(right) > 0:
            order = 1
        elif len(left) == 0 and len(right) == 0:
            order = 0
        else:
            for i in range(len(left)):
                order = compare(left[i], right[i])
                if order != 0:
                    break
                if len(right) == i + 1 and len(left) > i + 1:
                    order = -1
                    break
                elif len(left) == i + 1 and len(right) > i + 1:
                    order = 1
                    break


    return order



if __name__ == "__main__":
    main()


