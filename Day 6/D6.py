# Advent of Code 2022 - Day 6
# Eetu Knutars / @knuutti

def main():

    N = 14  # the length of the desired queue (4 for part 1, 14 for part 2)

    file_name = "D6_data.txt"

    data_file = open(file_name, 'r')
    data = data_file.readline()

    char_queue = [None] * (N-1)   # stores the previous N characters
    dublicate = True        # stores the info whether there is a dublicate in the queue

    for i,char in enumerate(data):

        # Processed character is already in the queue, update the queue and go to the next one
        if char in char_queue:
            char_queue.pop(0)
            char_queue.insert(N-2, char)
            continue

        # Loop for looking for dublicates in the existing queue
        for j,old_char in enumerate(char_queue):
            
            # A dublicate is found -> update the value and break the loop
            if old_char in char_queue[j+1:]:
                dublicate = True
                break

            dublicate = False

        # If there is a dublicate or the queue length is less than N, update the queue
        if dublicate or not char_queue[0]:
            char_queue.pop(0)
            char_queue.insert(N-2, char)

        # Processing has finished
        else:
            print(f"Number of processed characters: {i+1}")
            break



if __name__ == "__main__":
    main()