fname = "day05.txt"
file = open(fname, 'r')
data = file.read().splitlines()

ranges = []
row_count = len(data)
endpoints = {}
break_index = data.index("")

# Read the ranges
for i in range(break_index):
    value_range = data[i].split("-")
    range_start, range_end = int(value_range[0]), int(value_range[1])
    endpoints[range_start] = 1
    endpoints[range_end] = 1
    ranges.append((range_start, range_end))

# Part 1: check if item is in any range
total_fresh = 0
for i in range(break_index+1, row_count):
    ingredient = int(data[i])
    for r in ranges:
        if ingredient <= r[1] and ingredient >= r[0]:
            total_fresh += 1
            break
    
print("Silver:", total_fresh)

# Part 2: find the total number of valid items in ranges
# I used divide-and-conquer approach, splitting all ranges into subranges

# First round of processing split into subranges
subranges = {}
for r in ranges:
    subendpoints = []
    for p in sorted(endpoints):
        if p > r[1]: break
        if p < r[0]: continue
        
        subendpoints.append(p)
    
    for i in range(len(subendpoints)-1):
        subranges[(subendpoints[i], subendpoints[i+1])] = subendpoints[i]

    # Handling the ranges with only one value
    if r[0] == r[1]: subranges[(r[0],r[1])] = r[0]


# Second round of processing: combine connected subranges
processed_ranges = []
sorted_subranges = sorted(subranges)
while len(sorted_subranges) > 1:
    if sorted_subranges[0][1] == sorted_subranges[1][0]:
        sorted_subranges[1] = (sorted_subranges[0][0], sorted_subranges[1][1])
        sorted_subranges.pop(0)
    else: processed_ranges.append(sorted_subranges.pop(0))
processed_ranges.append(sorted_subranges[0])

# Finally go through all processed ranges and calculate the number of items in each
total_values = 0
for r in processed_ranges:
    total_values += 1+r[1]-r[0]

print("Gold:", total_values)






