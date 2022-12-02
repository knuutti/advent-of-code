# Advent of Code 2022 - Day 1
# Eetu Knutars / @knuutti

import time

def main():
    data_file = open("D1_data.txt", 'r')
    calories = [] # stores the calories for each elf
    calories_elf = 0 # calory count for one elf in each iteration
    
    # Loop for going through the data
    while True:
        row = data_file.readline()
        # If the row only consists of the line break, store the value and move to the next elf
        if row == "\n":
            calories.append(calories_elf)
            calories_elf = 0
        # No more data, store the value for the last elf and break the loop
        elif len(row) == 0:
            calories.append(calories_elf)
            break
        # Line consists of calory value, store the value
        else:
            calories_elf += int(row)

    # Printing the analysis
    print(f"Max: {sorted(calories)[len(calories)-1]}")
    print(f"Sum of first three: {sum(sorted(calories)[len(calories)-3:len(calories)])}")

    return

if __name__ == "__main__":
    main()