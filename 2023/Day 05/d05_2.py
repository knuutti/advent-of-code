def main():   
    fname = "./2023/Day 05/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    seed_info = [int(x) for x in data[0].lstrip("seeds: ").split()]
    seed_ranges = []
    for i in range(0, len(seed_info), 2):
        seed_ranges.append([seed_info[i], seed_info[i]-1+seed_info[i+1]])

    #print(seed_ranges)

    conversion_ranges = []
    topic = False
    for line in data[3:]:
        #print(line)
        if topic: # header row
            topic = False
            continue
        if len(line) == 0: # empty row
            seed_ranges = new_ranges(seed_ranges, conversion_ranges)
            conversion_ranges = []
            topic = True
            continue
        
        line = [int(x) for x in line.split()]
        conversion_ranges.append([line[1], line[1]+line[2]-1, line[0]-line[1]]) # start, end, delta
    
    seed_ranges = new_ranges(seed_ranges, conversion_ranges)
    value = seed_ranges[0][0]
    for seed in seed_ranges:
        if seed[0] < value:
            value = seed[0]

    print(value)




def new_ranges(seed_ranges: list, conversion_ranges: list):
        #print(seed_ranges, conversion_ranges)
        new_seed_ranges = []
        while len(seed_ranges) > 0: # using while since we'll add stuff to seed_ranges still
            seed = seed_ranges.pop(0)
            x = len(new_seed_ranges)
            for conversion in conversion_ranges:

                if seed[0] == conversion[0]:
                    new_seed_ranges.append([seed[0]+conversion[2],seed[0]+conversion[2]])
                    seed_ranges.append([seed[0]+1,seed[1]])
                    break
                elif seed[0] == conversion[1]:
                    new_seed_ranges.append([seed[0]+conversion[2],seed[0]+conversion[2]])
                    break
                elif seed[1] == conversion[0]:
                    new_seed_ranges.append([seed[1]+conversion[2],seed[1]+conversion[2]])
                    break
                elif seed[1] == conversion[1]:
                    new_seed_ranges.append([seed[1]+conversion[2],seed[1]+conversion[2]])
                    seed_ranges.append([seed[0],seed[1]-1])
                    break

                if conversion[0]>seed[0] and conversion[1]<seed[1]: # conversion range inside seed range
                    #print("1")
                    new_seed_ranges.append([conversion[0]+conversion[2],conversion[1]+conversion[2]])
                    seed_ranges.append([seed[0],conversion[0]-1])
                    seed_ranges.append([conversion[1]+1, seed[1]])
                    break

                elif conversion[0]<seed[0] and conversion[1]>seed[1]: # seed range inside conversion range
                    #print("2")                      
                    new_seed_ranges.append([seed[0]+conversion[2],seed[1]+conversion[2]])
                    break

                elif conversion[0]>seed[0] and conversion[0]<seed[1] and conversion[1]>seed[1]: # open right side
                    #print("3")
                    new_seed_ranges.append([conversion[0]+conversion[2],seed[1]+conversion[2]])
                    seed_ranges.append([seed[0],conversion[0]-1])
                    break

                elif conversion[0]<seed[0] and conversion[1]>seed[0] and conversion[1]<seed[1]: # open left side
                    #print("4")
                    new_seed_ranges.append([seed[0]+conversion[2],conversion[1]+conversion[2]])
                    seed_ranges.append([conversion[1]+1,seed[1]])
                    break

            if x == len(new_seed_ranges):
                new_seed_ranges.append(seed)

                  
        return new_seed_ranges
                  

if __name__ == "__main__":
    
    main()