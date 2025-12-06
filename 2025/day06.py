from numpy import zeros, prod

fname = "day06.txt"
file = open(fname, 'r')
data = file.read().splitlines()

operators = data[-1]
numbers = data[0:-1]

operators = operators.split()
M = len(operators)
N = len(numbers)

## PART 1

# Load numbers into numpy matrix for easier access
number_matrix = zeros((N,M))
for i,line in enumerate(numbers):
    nums = line.split()
    for j,n in enumerate(nums):
        number_matrix[i,j] = int(n)

# Calculate the sums and prods
total = 0
for i,o in enumerate(operators):
    if o == "+":
        total += sum(number_matrix.T[i,:])
    else:
        total += prod(number_matrix.T[i,:])

print("Silver:", int(total))

## PART 2

# Finding first the maximum character length
# (This could have been done much more elegantly)
max_len = 0
for line in numbers:
    if len(line) > max_len: max_len = len(line)

# Initialize a list for storing numbers for every column
numbers_in_columns = [""] * max_len

# Load numbers to the list and find indeces where there is empty column
breakpoints = []
for i in range(max_len):
    for j in range(N):
        if numbers[j][i].isnumeric():
            numbers_in_columns[i] += numbers[j][i]
    if numbers_in_columns[i] == "":
        breakpoints.append(i)

# Load the processed numbers into separate cells
final_numbers = []
final_numbers.append(numbers_in_columns[0:breakpoints[0]])
for i in range(len(breakpoints)-1):
    final_numbers.append(numbers_in_columns[breakpoints[i]+1:breakpoints[i+1]])
final_numbers.append(numbers_in_columns[breakpoints[-1]+1:])

# Calculate sums and prods
total_gold = 0
for i,n in enumerate(final_numbers):
    nums = list(map(lambda i: int(i), n))
    if operators[i] == "+":
        total_gold += sum(nums)
    else:
        total_gold += prod(nums)

print("Gold:", total_gold)