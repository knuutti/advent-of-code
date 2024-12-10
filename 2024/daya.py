if __name__ == "__main__":

    data = open("input_daya.txt",'r').read().splitlines()
    R = len(data)
    C = len(data[0])

    def helper(node, value, total, mode):
        if value == 9 and (node not in V or mode == 1): 
            V[node] = 1
            return total + 1
        if node[0] > 0 and data[node[0]-1][node[1]] == value + 1: 
            total = helper((node[0]-1,node[1]), value+1, total, mode)
        if node[1] > 0 and data[node[0]][node[1]-1] == value + 1: 
            total = helper((node[0],node[1]-1), value+1, total, mode)
        if node[0] < R-1 and data[node[0]+1][node[1]] == value + 1: 
            total = helper((node[0]+1,node[1]), value+1, total, mode)
        if node[1] < C-1 and data[node[0]][node[1]+1] == value + 1: 
            total = helper((node[0],node[1]+1), value+1, total, mode)
        return total

    new_data = []
    start_nodes = {}
    for i in range(R):
        new_data.append([])
        for j in range(C):
            new_data[i].append(int(data[i][j]))
            if data[i][j] == "0":
                start_nodes[(i,j)] = 1
    data = new_data

    V = {}
    gold, silver = 0, 0
    for node in start_nodes:
        curr = 0
        V = {}
        silver += helper(node, 0, 0, 0)
        gold += helper(node, 0, 0, 1)

    print("Silver:", silver)
    print("Gold:", gold)