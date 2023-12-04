def main():   
    
    fname = "./2023/Day 04/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

  
    total = 0
    copies = []
    for i in range(len(data)):
        copies.append(1)

    for i,line in enumerate(data):
        wins = 0
        winning = []
        line = line.split(": ")
        line = line[1].split(" | ")
        for num in line[0].split(" "):
            if num == "":
                continue
            winning.append(int(num))
        for num in line[1].split(" "):
            if num == "":
                continue
            if int(num) in winning:
                wins += 1
        if wins:
            total += 2**(wins-1)
            for j in range(i+1, i+wins+1):
                if j < len(copies):
                    copies[j] += copies[i]*1
    
    print(total)
    print(sum(copies))




    
if __name__ == "__main__":
    main()