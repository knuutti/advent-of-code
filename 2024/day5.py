import numpy as np

data = open("input_day5.txt", 'r').read().splitlines()

# Lil' spaghetti code, might try to clean up later...

rules = {}
numbers = []
updates = []

for i in data:
    if i == "": continue
    i = i.split("|")
    if len(i) == 1: 
        new_update = []
        for x in i[0].split(","):
            numbers.append(int(x))
            new_update.append(int(x))
        updates.append(new_update)
        continue
    numbers.append(int(i[0]))
    numbers.append(int(i[1]))
    if not int(i[1]) in rules: rules[int(i[1])] = [int(i[0])]
    else: rules[int(i[1])].append(int(i[0]))

# List of all numbers present
numbers = list(set(numbers))

# Dumping all rules into a matrix
M = np.zeros((len(numbers), len(numbers)))
for r in rules:
    for c in rules[r]:
        M[numbers.index(r),numbers.index(c)] = 1

silver, gold = 0, 0
for update in updates:
    indeces = []
    for number in update:
        indeces.append(numbers.index(numbers))

    # Tracking whether number is in right place
    s = 0
    new_list = [0] * len(update) # sorted update is stored here
    for i in range(len(indeces)):
        s += sum(M[indeces[i],indeces[i:]])
        # Sort based on the number sum in the matrix
        new_list[int(np.sum(M[:,indeces][indeces[i]]))] = numbers[indeces[i]]
    if s == 0: silver += update[len(update)//2]
    else: gold += new_list[len(new_list)//2]

print("Silver:", silver)
print("Gold", gold)
