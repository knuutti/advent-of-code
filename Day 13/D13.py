import json

def main():

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
            print("Order", 1+i*3)
            score += i+1
        else:
            print("Not Order", 1+ (i)*3)

    print(score)
            

def compare(left, right):

    order = 0

    # Converting singular integers to lists
    if type(left) is int and type(right) is not int:
            left = [left]
    elif type(right) is int and type(left) is not int:
            right = [right]
    
    #print("Compare", left, "vs", right)

    if type(left) is int:
        order = right - left
    else: # lists
        if len(right) == 0 and len(left) > 0:
            return -1
        elif len(left) == 0 and len(right) > 0:
            return 1
        for i in range(len(left)):
            order = compare(left[i], right[i])
            if order != 0:
                break
            if len(right) == i + 1 and len(left) > i + 1:
                order = -1
                break

    return order

main()


