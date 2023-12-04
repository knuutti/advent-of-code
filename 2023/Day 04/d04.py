def main():   
    
    fname = "./2023/Day 04/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    total = 0
    copies = [1 for _ in range(len(data))] 

    for i,line in enumerate(data):

        line = line.split(": ")
        line = line[1].split(" | ")
        winning_numbers = check_winning_numbers(line)
        wins = check_wins(line, winning_numbers)

        if wins:
            total += 2**(wins-1) # update the points
            for j in range(i+1, i+wins+1): # update the number of copies
                if j < len(copies):
                    copies[j] += copies[i]*1
    
    print("Part 1:", total)
    print("Part 2:", sum(copies))


def check_winning_numbers(line):
    winning = []
    for num in line[0].split(" "):
        if num == "":
            continue
        winning.append(int(num))
    return winning

def check_wins(line, winning_numbers):
    wins = 0
    for num in line[1].split(" "):
        if num == "":
            continue
        if int(num) in winning_numbers:
            wins += 1
    return wins

    
if __name__ == "__main__":
    main()