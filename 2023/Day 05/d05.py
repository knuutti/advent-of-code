def main():   
    fname = "./2023/Day 05/example.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()

    min_location = 10000000

    seeds = get_seeds(data) # gets range of seeds
    print(seeds)
    seeds = get_conversion(data.index("seed-to-soil map:"), data, seeds)
    print(seeds)
    
    seeds = get_conversion(data.index("soil-to-fertilizer map:"), data, seeds)
    print(seeds)
    seeds = get_conversion(data.index("fertilizer-to-water map:"), data, seeds)
    print(seeds)
    seeds = get_conversion(data.index("water-to-light map:"), data, seeds)
    print(seeds)
    seeds = get_conversion(data.index("light-to-temperature map:"), data, seeds)
    print(seeds)
    seeds = get_conversion(data.index("temperature-to-humidity map:"), data, seeds)
    print(seeds)
    seeds = get_conversion(data.index("humidity-to-location map:"), data, seeds)
    print(seeds)

def get_seeds(data):
    line = data[0].split()
    line.pop(0)
    
    nums = [int(x) for x in line]
    seeds = []
    for i in range(0,len(nums)//2+1,2):
        seeds.append([nums[i],nums[i]+nums[i+1]])

    return seeds

def get_conversion(index, data, seeds):
    conversions = []
    while index < len(data)-1:
        index += 1
        if len(data[index]) == 0:
            break
        [dest, src, ran] = [int(x) for x in data[index].split()]

        conversions.append([src, src+ran, dest-src])

    #print(conversions)
    converted = []

    

    for seed in seeds:
        

        # conv0 = min source
        # conv1 = max source
        # conv2 = conversion term (src -> dest)
        #print("----------")
        #print(seed)
        #print(conversions)

        # given the range of seeds
        # get range of outcomes

        for conv in conversions:

            min_converted = 10000000
            max_converted = -1

            min_local = seed[0]
            max_local = seed[1]
            # seed range
            min_seed = seed[0]
            max_seed = seed[1]

            #print(min_seed, max_seed, conv)

            # left seed range OUTSIDE conversion range
            if min_seed <= conv[0] and max_seed >= conv[0]:
                if conv[0]+conv[2] < min_converted:
                    min_converted = conv[0]+conv[2]
            # left seed range INSIDE conversion range
            elif min_seed >= conv[0] and min_seed <= conv[1]:
                min_local = min_seed + conv[2]
                if min_seed + conv[2] < min_converted:
                    min_converted = min_seed + conv[2]
            
            # right seed range INSIDE conversion range
            if max_seed <= conv[1] and max_seed >= conv[0]:
                max_local = max_seed + conv[2]
                if max_seed + conv[2] > max_converted:
                    max_converted = max_seed + conv[2]
            # right seed range OUTSIDE conversion range
            elif max_seed > conv[1] and min_seed <= conv[1]:
                if conv[1]+conv[2] > max_converted:
                    max_converted = conv[1]+conv[2]

        
            if min_converted == 10000000:
                min_converted = seed[0]
            if max_converted == -1:
                max_converted = seed[1]

            #print(min_converted, max_converted)

            #print(min_converted, max_converted)



            if [min_converted, max_converted] not in converted:
                converted.append([min_converted, max_converted])

            # if [min_local, max_local] not in converted:
            #     converted.append([min_local, max_local])



    return converted

if __name__ == "__main__":
    
    main()