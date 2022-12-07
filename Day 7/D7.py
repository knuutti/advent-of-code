# Advent of Code 2022 - Day 7
# Eetu Knutars / @knuutti

def main():

    file_name = "D7_data.txt"

    data_file = open(file_name, 'r')
    data = data_file.read().splitlines()
    data_file.close()

    directories = {"/": 0}
    current_path = "/"

    for line in data:
        units = line.split()
        if units[0] == "$":
            if units[1] == "cd":
                if units[2]=='..':
                    # moving back in the hierarchy
                    break_index = len(current_path) - current_path[len(current_path)-2::-1].find("/") - 1
                    current_path = current_path[:break_index]
                elif units[2] == "/":
                    current_path = "/"
                else:
                    current_path += units[2] + "/"
        else:
            if units[0] == "dir":
                # storing the info of a directory existing
                directories[current_path + units[1] + "/"] = 0
            else:
                # files are stored to a dictionary with their full path
                directory_path = current_path
                file_size = int(units[0])
                while True:
                    if len(directory_path) < 2:
                        directories["/"] += file_size
                        break
                    else:
                        directories[directory_path] += file_size

                    break_index = len(directory_path) - directory_path[len(directory_path)-2::-1].find("/") - 1
                    directory_path = directory_path[:break_index]
                    
    # Part 1 solution
    total = 0
    for dire in directories:
        if directories.get(dire) < 100001:
            total += directories.get(dire)
    print("Part 1:", total)

    # Part 2 solution
    total_space = 70000000
    minimum_space = 30000000
    used_space = directories.get("/")
    required_space = used_space - (total_space - minimum_space)
    for value in sorted(directories.values()):
        if value >= required_space:
            required_space = value
            break
    print("Part 2:", required_space)

    return 

if __name__ == "__main__":
    main()