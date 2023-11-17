import re

class BingoBoard():
    def __init__(self, matrix):
        self.lines = [
            matrix[0],
            matrix[1],
            matrix[2],
            matrix[3],
            matrix[4],
            [matrix[0][0], matrix[1][0], matrix[2][0], matrix[3][0], matrix[4][0]],
            [matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1], matrix[4][1]],
            [matrix[0][2], matrix[1][2], matrix[2][2], matrix[3][2], matrix[4][2]],
            [matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3], matrix[4][3]],
            [matrix[0][4], matrix[1][4], matrix[2][4], matrix[3][4], matrix[4][4]]
        ]

    # Function to determine if board wins
    # If number is found on the board, remove it from the lines
    # Returns true is some column has needs no more numbers to be hit
    # Otherwise returns false
    def check(self, number):
        for line in self.lines:
            if number in line:
                line.remove(number)
                if len(line) == 0:
                    return True
        return False


def main():

    fname = "d4_data.txt"
    file = open(fname, 'r')
    content = file.read().splitlines()
    file.close()

    # I will just do the number comparisons as strings, could also convert numbers
    # to integers but this method works for the task as well

    # Numbers to be drawn
    numbers = content[0].split(",")

    # Creation of bingo boards
    boards: list[BingoBoard] = []
    temp = []
    for row in content[2:]:
        if len(row) == 0:
            continue
        temp.append(re.split("\s+", row.lstrip(" ")))
        if len(temp) == 5:
            boards.append(BingoBoard(temp))
            temp = []

    # Starting the game
    s = 0
    n = 0
    wins = []
    board_wins = {}
    # Iterating through each number
    for number in numbers:
        # Checking each board for possible bingo
        for i,board in enumerate(boards):
            if board.check(number):
                # If bingo is hit, store the current number
                n = int(number)
                # Calculate the sum of unmarked numbers
                for row in board.lines[0:5]:
                    for mark in row:
                        s += int(mark)
                # If this is the first bingo of the board, store score to a list
                if not i in board_wins:
                    board_wins[i] = 1
                    wins.append(s*n)
                s = 0

    print("Part 1:", wins[0])
    print("Part 2:", wins[-1])

    return

if __name__ == "__main__":
    main()