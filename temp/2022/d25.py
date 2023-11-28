# Advent of Code 2022 - Day 25
# Eetu Knutars / @knuutti

# Helper function for the addition, this returns the remainder of the 
# current index and carry value to the next index
def determine_remainder(s):
    a = 0
    ind = s < 0 # dealing with negatives
    s = abs(s)
    if s%5 > 2:
        a = 1
    if not ind:
        return (s//5 + a, s - ((s//5)+a)*5)
    return (-1*(s//5 + a), -1*(s - ((s//5)+a)*5))

# Function for converting to desimal
def decode(c):
    if c in ["0", "1", "2"]:
        return int(c)
    elif c == "-":
        return -1
    return -2

# Function for converting from decimal
def code(c):
    if c in [0, 1, 2]:
        return str(c)
    elif c == -1:
        return "-"
    return "="

def main():

    fname = "d25_data.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    file.close()

    # Inversing the rows to aid processing and 
    max_len = 0
    inv = []
    for row in data:
        if len(row) > max_len:
            max_len = len(row)
        inv.append(row[::-1])

    # Storing the final number to a string
    result = "" 

    # Adding up all the numbers index by index
    s = 0
    for i in range(0, max_len + 1):
        # Going through the i:th index of each number
        for number in inv:
            if len(number) >= i + 1:
                # Adding to the total sum of the index
                s += decode(number[i])

        # Determine remainder and carry values
        temp = determine_remainder(s)
        
        # Adding the remainder to the result string
        result += code(temp[1]) 

        # Carrying the carry value to the next index
        s = temp[0]

    print("Part 1:", result[::-1].lstrip("0"))



if __name__ == "__main__":
    main()