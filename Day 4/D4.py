def main():
    
    data_file = open("D4_data.txt", "r")
    data = data_file.readlines()
    data_file.close()

    sum_full = 0    # part 1 result
    sum_overlap = 0 # part 2 result

    for pair in data:
        
        pair = pair.split(",")

        # Defining the start and end points for the first assignment
        p1 = pair[0].split("-")
        p1_start = int(p1[0])
        p1_end = int(p1[1])
        
        # Defining the start and end points for the second assignment
        p2 = pair[1].split("-")
        p2_start = int(p2[0])
        p2_end = int(p2[1])

        # If one of the assignments is fully contained in the other
        if (p1_start >= p2_start and p1_end <= p2_end) or (p2_start >= p1_start and p2_end <= p1_end):
            sum_full += 1

        # If there's any overlapping between assignments
        if (p1_start >= p2_start and p2_end >= p1_start) or (p2_start >= p1_start and p1_end >= p2_start):
            sum_overlap += 1

    # Printing the results
    print(f"Fully contained pairs: \t{sum_full}")
    print(f"Overlapping pairs: \t{sum_overlap}")
    
    return

if __name__ == "__main__":
    main()