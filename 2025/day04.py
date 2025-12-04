from numpy import array, zeros
from scipy.signal import convolve2d

fname = "day04.txt"
file = open(fname, 'r')
data = file.read().splitlines()

R, C = len(data), len(data[0])

rolls = {}

kernel = array([[1,1,1],
          [1,0,1],
          [1,1,1]])

data_ext = zeros((R+2,C+2))

for row in range(R):
    for column in range(C):
        if data[row][column] == "@":
            rolls[(row,column)] = 1
            data_ext[row+1,column+1] = 1

total_rolls = 0

flag = False

while True:

    co = convolve2d(data_ext, kernel, mode='same')

    round_total = 0

    for roll in rolls.copy():
        if co[roll[0]+1,roll[1]+1] < 4:
            round_total += 1
            del rolls[roll]
            data_ext[roll[0]+1,roll[1]+1] = 0

    if round_total == 0:
        break

    total_rolls += round_total

    if flag == False:
        print("Silver:", round_total)
        flag = True


print("Gold:", total_rolls)