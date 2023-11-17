# Advent of Code 2022 - Day 7
# Eetu Knutars / @knuutti

def main():

    file_name = "d07_data.txt"

    data_file = open(file_name, 'r')
    data = data_file.read().splitlines()
    data_file.close()

    directories = {"/": 0}
    current_path = "/"

    # The directories are stored with their whole paths to the dictionary
    # This solves the problem with dublicate directory names (which I fought with for a while...)


    # Looping through the data and storing the file structure (with file sizes) to a dictionary
    for line in data:
        units = line.split()
        if units[0] == "$":
            # Command line (in the script we only care about the "cd" command)
            if units[1] == "cd":
                # Changing directories by modifying the current path variable
                if units[2]=='..':
                    # Stripping the last directory from the path (moving back in hierarchy)
                    break_index = len(current_path) - current_path[len(current_path)-2::-1].find("/") - 1
                    current_path = current_path[:break_index]
                elif units[2] == "/":
                    # Returning to the root directory
                    current_path = "/"
                else:
                    # Adding the desired directory to the path (moving to the next directory)
                    current_path += units[2] + "/"
        else:
            # Print line (results are either directories or files)
            if units[0] == "dir":
                # A directory is listed
                if current_path + units[1] + "/" not in directories:
                    # The directory is a new one, adding it to the dictionary
                    directories[current_path + units[1] + "/"] = 0
            else:
                # A file is listed, increasing the size for all the directories in the current path
                file_size = int(units[0])

                directory_path = current_path
                while True:
                    # Looping until we hit the root directory /
                    if len(directory_path) < 2:
                        # Root directory
                        directories["/"] += file_size
                        break
                    else:
                        # Non-root directory
                        directories[directory_path] += file_size

                    # Stripping the last directory from the path for the next iteration
                    break_index = len(directory_path) - directory_path[len(directory_path)-2::-1].find("/") - 1
                    directory_path = directory_path[:break_index]
                    
    # Part 1 solution
    total = 0
    for dire in directories:
        # Looping through the directies and summing up the ones with size of at most 100 000
        if directories.get(dire) < 100001:
            total += directories.get(dire)
    print("Part 1:", total)

    # Part 2 solution
    total_space = 70000000
    minimum_space = 30000000
    used_space = directories.get("/")
    required_space = used_space - (total_space - minimum_space)
    for value in sorted(directories.values()):
        # Looping through the sorted directories until we find one with size at least the required amount
        if value >= required_space:
            required_space = value
            break
    print("Part 2:", required_space)

    return 

if __name__ == "__main__":
    main()