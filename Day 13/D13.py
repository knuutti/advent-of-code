#   Advent of Code 2022 - Day 13
#   Eetu Knutars / @knuutti

import json

# only Part 1

def main():

    sorted_list = []

    file_name = "D13_data.txt"
    file = open(file_name, 'r')
    data = file.read().splitlines()
    file.close()

    # Strings to data types
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
            score += i+1

    print("Part 1:", score)

    for i,pair in enumerate(M):
        order = -1
        for i,item in enumerate(sorted_list):
            order = compare(pair[0], item)
            if order >= 0:
                sorted_list.insert(i, pair[0])
                break
        if order < 0:
            sorted_list.append(pair[0])

        for i,item in enumerate(sorted_list):
            order = compare(pair[1], item)
            if order >= 0:
                sorted_list.insert(i, pair[1])
                break
            else:
                order = -1
        if order < 0:
            sorted_list.append(pair[1])

    loc_1, loc_2 = None, None

    for i,item in enumerate(sorted_list):
            order = compare([[2]], item)
            if order >= 0:
                loc_1 = i + 1
                break

    for i,item in enumerate(sorted_list):
            order = compare([[6]], item)
            if order >= 0:
                loc_2 = i + 2
                break


    print("Part 2:", loc_1*loc_2)
    

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

main()


