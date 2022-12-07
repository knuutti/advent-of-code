# Advent of Code 2022 - Day 6
# Eetu Knutars / @knuutti

import time

def analyse(file_name, N):

    data_file = open(file_name, 'r')
    data = data_file.readline()

    for i in range(N, len(data)):

        # Removing the dublicate charactes in the past N characters
        # If length of the dictionary is N, all characters are unique
        if len(dict.fromkeys(data[i-N:i])) == N:
            print(f"Number of processed characters (N = {N}): {i}")
            break



if __name__ == "__main__":
    
    start = time.time()

    file_name = "bigboy.txt"
    analyse(file_name, 4)
    analyse(file_name, 14)

    end = time.time()

    print(f"Running time:\n{end-start:.1f}s")