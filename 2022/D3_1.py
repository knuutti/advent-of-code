# Advent of Code 2022 - Day 3
# Eetu Knutars / @knuutti

# Part 1

def main():

    data_file = open("D3_data.txt", 'r')
    data = data_file.readlines()
    data_file.close()

    sum_all = 0

    for rucksack in data:

        l = len(rucksack) // 2  # compartment length
        
        # Defining the compartments
        v1 = rucksack[0:l]
        v2 = rucksack[l:len(rucksack)]

        for char in v1:

            if char in v2:

                # Calculating the priority value based on the ASCII value
                if ord(char) > 90:
                    sum_all+=(ord(char)-96)
                else:
                    sum_all+=(ord(char)-38)

                break

    print(f"Sum of the priorities: {sum_all}")



    return

if __name__ == "__main__":
    main()