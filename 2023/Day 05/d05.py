# Advent of Code 2023 - Day 5
# Eetu Knutars / @knuutti

# First real challenge of this year, quite fun after all

def main():   
    fname = "./2023/Day 05/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    print("Part 1:", analyse(seeds(data,0), data))
    print("Part 2:", analyse(seeds(data,1), data))
    return

# Returns a list consisting all ranges of seeds
def seeds(data, mode):
        s = [int(x) for x in data[0].lstrip("seeds: ").split()]
        input_ranges = []
        for i in range(0, len(s), mode+1):
            input_ranges.append([s[i], s[i]-1+s[i+1] if mode else s[i]])
        return input_ranges

# Returns the lowest possible value after the last conversion
def analyse(input_ranges, data):
    output_ranges = []
    for line in data[3:]:
        if not len(line): # empty row
            input_ranges = get_new_ranges(input_ranges, output_ranges)
            output_ranges = []
        elif line[0].isnumeric():
            line = [int(x) for x in line.split()]
            output_ranges.append([line[1], line[1]+line[2]-1, line[0]-line[1]]) # start, end, delta
    input_ranges = get_new_ranges(input_ranges, output_ranges)
    
    return min(map(lambda a : a[0], input_ranges)) # practicing the use of lambda and map functions ...

# Updating the possible ranges based on conversion ranges
def get_new_ranges(input_ranges: list, output_ranges: list):
        new = []
        while len(input_ranges) > 0: # using while since we'll add stuff to input_ranges still

            [input_start, input_end] = input_ranges.pop(0)
            x = len(new)

            for [output_start, output_end, delta] in output_ranges:
                
                if input_start == output_start:
                    new.append([input_start+delta,input_start+delta])
                    input_ranges.append([input_start+1,input_end])

                elif input_start == output_end:
                    new.append([input_start+delta,input_start+delta])
                
                elif input_end == output_start:
                    new.append([input_end+delta,input_end+delta])
                
                elif input_end == output_end:
                    new.append([input_end+delta,input_end+delta])
                    input_ranges.append([input_start,input_end-1])
                
                elif output_start>input_start and output_end<input_end: # conversion range inside seed range
                    new.append([output_start+delta,output_end+delta])
                    input_ranges.append([input_start,output_start-1])
                    input_ranges.append([output_end+1, input_end])
                
                elif output_start<input_start and output_end>input_end: # seed range inside conversion range 
                    new.append([input_start+delta,input_end+delta])
                
                elif output_start>input_start and output_start<input_end and output_end>input_end: # open right side
                    new.append([output_start+delta,input_end+delta])
                    input_ranges.append([input_start,output_start-1])
                
                elif output_start<input_start and output_end>input_start and output_end<input_end: # open left side
                    new.append([input_start+delta,output_end+delta])
                    input_ranges.append([output_end+1,input_end])
    
                if len(new) != x: break
                    
            if x == len(new): # input didn't change in any conversion -> store old boundaries
                new.append([input_start, input_end]) 

        return new
                  

if __name__ == "__main__":
    
    main()