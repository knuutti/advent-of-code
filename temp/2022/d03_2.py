# Advent of Code 2022 - Day 3
# Eetu Knutars / @knuutti

# Part 2

def main():

    data_file = open("d03_data.txt", 'r')

    sum_all = 0

    while True:

        # Storing the three lines to separate variables
        v1 = data_file.readline()

        # No more data, breaking the loop
        if len(v1) == 0:
            break

        # Reading the other two lines
        v2 = data_file.readline()
        v3 = data_file.readline()

        # Finding the common character
        for char in v1:

            if char in v2 and char in v3:

                if ord(char) > 90:
                    sum_all+=(ord(char)-96)
                else:
                    sum_all+=(ord(char)-38)

                break

    print(f"Sum of the priorities: {sum_all}")

    return

if __name__ == "__main__":
    main()