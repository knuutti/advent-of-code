# Advent of Code 2022 - Day 6
# Eetu Knutars / @knuutti

def analyse(file_name, N):

    data_file = open(file_name, 'r')
    data = data_file.readline()

    for i in range(len(data)):

        # Removing the dublicate charactes in the past N characters
        unique_chars = list( dict.fromkeys(data[i-N:i]) )

        # If all characters were unique, we found the last character
        if len(unique_chars) == N:
            print(f"Number of processed characters (N = {N}): {i}")
            break



if __name__ == "__main__":
    file_name = "D6_data.txt"
    analyse(file_name, 4)
    analyse(file_name, 14)