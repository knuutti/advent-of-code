def main():   
    fname = "./2023/Day 04/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    points = 0
    copies = [1 for _ in range(len(data))] 

    for i,line in enumerate(data):
        line = line.split(":")[1].split("|")
        winning_numbers = check_winning_numbers(line[0]) # get list of winning numbers
        wins = check_wins(line[1], winning_numbers) # get number of wins
        if wins:
            points += 2**(wins-1) # update the points
            for j in range(i+1, i+wins+1): # update the number of copies
                if j < len(copies):
                    copies[j] += copies[i]*1 # multiply by copies of current card
    
    print("Part 1:", points)
    print("Part 2:", sum(copies))

def check_winning_numbers(line):
    winning = []
    for num in line.split():
        winning.append(num)
    return winning

def check_wins(line, winning_numbers):
    wins = 0
    for num in line.split():
        if num in winning_numbers:
            wins += 1
    return wins

if __name__ == "__main__":
    main()