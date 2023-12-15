# Advent of Code 2023 - Day 13
# Eetu Knutars / @knuutti

# Good mirrors

def main():
    fname = "./2023/Day 15/input.txt"
    file = open(fname, 'r')
    data = file.read().split(',')

    boxes = [[] for _ in range(256)]
    result = 0
    for w in data:
        value = 0
        for c in w:
            value += ord(c)
            value *= 17
            value = value % 256

        result += value

        if w.find("=") == -1:
            w = w.split("-")
        else: 
            w = w.split("=")

        label_value = 0
        #print(w[0])
        for c in w[0]:
            #print(c)
            label_value += ord(c)
            label_value *= 17
            label_value = label_value % 256

        if len(w[1]):
            index = len(boxes[label_value])
            for i,lens in enumerate(boxes[label_value]):
                if w[0] in lens.split():
                    boxes[label_value].pop(i)
                    index = i
                    break
            boxes[label_value].insert(index, w[0] + " " + w[1])
        else:
            for i,lens in enumerate(boxes[label_value]):
                if w[0] in lens.split():
                    boxes[label_value].pop(i)
                    break

        #print(boxes[0], boxes[1], boxes[3])

    

    gold = 0
    for i,box in enumerate(boxes):
        for j,lens in enumerate(box):
            f_power = (i+1)*(j+1)*(int(lens.split()[1]))
            #print(i+1, j+1, int(lens.split()[1]))
            gold += f_power
            
    print("Part 1:",result)
    print("Part 2:",gold)

if __name__ == '__main__':
    main()