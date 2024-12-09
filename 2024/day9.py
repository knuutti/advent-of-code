def init_list(data):
    sizes = [int(x) for x in data[::2]]
    empty = [int(x) for x in data[1::2]]
    empty.append(0)
    x = [-1] * (sum(sizes)+sum(empty))
    empty_lower = []
    empty_upper = []
    index = 0
    id = 0
    for i in range(len(sizes)):
        for j in range(sizes[i]):
            x[index+j] = id
        id += 1
        index += sizes[i]
        empty_lower.append(index)
        empty_upper.append(index+empty[i]) # index where next value starts
        index += empty[i]
    return sizes, empty, x, empty_lower, empty_upper

def silver(data):
    sizes, _, x, el, eu = init_list(data)
    for j in range(len(x)-1,-1,-1):
        if x[j] == -1: continue
        for i in range(len(sizes)):
            if eu[i]-el[i] > 0 and el[i] < j:
                x[el[i]] = x[j]
                el[i] += 1
                x[j] = -1
                break
    silver = 0
    for i in range(sum(sizes)):
        silver += x[i]*i
    print("Silver:", silver)
                

def gold(data):
    sizes, empty, y, el, eu = init_list(data)
    j = 0
    for i in range(len(sizes)-1, 0, -1):
        oi = sum(empty[:i])+sum(sizes[:i])
        S = sizes[i]
        for j in range(i):
            if eu[j]-el[j] >= S:
                y[el[j]:el[j]+S] = [i] * S
                y[oi:oi+S] = [-1] * S
                el[j] += S
                break
    # Gold
    gold = 0
    for i,value in enumerate(y):
        gold += value*i*(value > 0)
    print("Gold:", gold)

if __name__ == "__main__":
    data = open("input_day9.txt", 'r').readline()
    silver(data)
    gold(data)