import math

def main():
    
    fname = "d5_data.txt"
    file = open(fname, 'r')
    content = file.read().splitlines()
    file.close()

    visited = {}
    counter = 0

    for row in content:
        points = row.split(" -> ")
        s = points[0].split(",")
        e = points[1].split(",")
        s = [int(s[0]), int(s[1])]
        e = [int(e[0]), int(e[1])]

        #print(s, e)

        # column
        if s[0] == e[0]:
            if s[1] > e[1]:
                s[1], e[1] = e[1], s[1]
            for i in range(s[1], e[1] + 1):
                if not (s[0], i) in visited:
                    visited[(s[0], i)] = 1
                else:
                    visited[(s[0], i)] += 1
                    if visited[(s[0], i)] == 2:
                        counter += 1
        
        # row
        elif s[1] == e[1]:
            if s[0] > e[0]:
                s[0], e[0] = e[0], s[0]
            for i in range(s[0], e[0] + 1):
                if not (i, s[1]) in visited:
                    visited[(i,s[1])] = 1
                else:
                    visited[(i,s[1])] += 1
                    if visited[(i,s[1])] == 2:
                        counter += 1

        # diagonal
        elif abs(s[1]-e[1]) == abs(s[0]-e[0]):
            #print(s,e)
            inc_hor = math.ceil((e[1]-s[1]) / abs(e[1]-s[1]))
            inc_ver = math.ceil((e[0]-s[0]) / abs(e[0]-s[0]))
            #print(inc_ver, inc_hor, abs(e[1]-s[1]), abs(e[0]-s[0]))
            diag_numbers = [[], []]
            #print(s[0], e[0] + inc_ver, inc_ver)
            #print(s[1], e[1] + inc_hor, inc_hor)
            for i in range(s[0], e[0] + inc_ver, inc_ver):
                diag_numbers[0].append(i)
            for i in range(s[1], e[1] + inc_hor, inc_hor):
                diag_numbers[1].append(i)
            #print(diag_numbers)

            for i in range(len(diag_numbers[0])):
                if not (diag_numbers[0][i], diag_numbers[1][i]) in visited:
                    visited[(diag_numbers[0][i], diag_numbers[1][i])] = 1
                else:
                    visited[(diag_numbers[0][i], diag_numbers[1][i])] += 1
                    if visited[(diag_numbers[0][i], diag_numbers[1][i])] == 2:
                        counter += 1
                        #print((diag_numbers[0][i], diag_numbers[1][i]))


    
    #print(visited)
    print("Part 1:", counter)

    return

if __name__ == "__main__":
    main()