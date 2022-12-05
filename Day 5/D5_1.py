def main():

    data_file = open("D5_data.txt", "r")

    # Storing the crate data in a matrix
    stacks = [None] * 9
    for i in range(9):
        stacks[i] = []

    # Looping through the starting positions
    while True:
        row = data_file.readline()

        # Breaking the loop once the instructions start
        if row[1] == "1":
            data_file.readline()
            break

        # If a crate is found, append the list
        for i in range(1, 34, 4):
            if row[i] != " ":
                stacks[(i-1)//4].append(row[i])
    
    # Looping through the instructions
    while True:
        instruction = data_file.readline()
        if len(instruction) == 0:
            break

        # Parsing the data
        temp = instruction.split(" ")
        amount = int(temp[1])
        start = int(temp[3])-1
        end = int(temp[5])-1

        # Doing the crate operation
        for i in range(amount):
            stacks[end].insert(0,stacks[start][0])
            stacks[start].pop(0)

    # Printing the result
    print("Top crates: ", end="")
    for i in range(9):
        print(stacks[i][0], end="")

if __name__ == "__main__":
    main()
