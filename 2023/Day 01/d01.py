# Advent of Code 2023 - Day 1
# Eetu Knutars / @knuutti

def main():   
    
    fname = "./2023/Day 01/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    file.close()

    print("Part 1:", sum_of_digits(data, 0))
    print("Part 2:", sum_of_digits(data, 1))

def find_digit(line, ran, mode):
        
        str_nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        for i in ran:
            # If an integer is found, return the value
            if line[i].isnumeric():
                return int(line[i])

            # Ignore spelled out digits if mode is set to 0
            if not mode:
                continue

            # Digit is spelled out
            for num in str_nums:
                # Checked substring depends whether we are looking for the first
                # digit or the last digit
                if ran[0] == 0:
                    substr = line[:i+1]
                else:
                    substr = line[i:]

                # If spelled out digit is in the substring, return the value
                if num in substr:
                    return str_nums[num]

def sum_of_digits(data, mode):

    total = 0
    for line in data:
        # Finding the first and last digit of each line
        first = find_digit(line, range(0, len(line)), mode)
        last = find_digit(line, range(len(line)-1, -1, -1), mode)
        if first and last:
            total += 10*first + last

    return total

if __name__ == "__main__":
    main()