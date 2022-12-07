from pathlib import PurePosixPath as Path

def analyse(file_name):

    data_file = open(file_name, 'r')
    data = data_file.read().splitlines()
    data_file.close()

    folders = {'/':0}
    files = {}
    current_path = Path('/')

    # Looping through the data
    for line in data:
        units = line.split()
        if units[0] == "$":
            if units[1] == "cd":
                if units[2]=='..':
                    # moving back in the hierarchy
                    current_path = current_path.parent 
                else:
                    # moving to the next directory in the hierarchy
                    current_path /= units[2]
        else:
            if units[0] == "dir":
                # storing the info of a directory existing
                folders[str(current_path/units[1])] = 0
            else:
                # files are stored to a dictionary with their full path
                files[str(current_path/units[1])] = int(units[0])

    # Looping through the folders updating their sizes
    for folder in folders:
        for file in files:
            # If folder is part of the path of a file, update the size
            if file.startswith(folder):
                folders[folder] += files[file]

    # Part 1
    total_sum = sum(size for size in folders.values() if size < 100001)
    print("Part 1:", total_sum)

    # Part 2
    available = 70000000
    unused = 30000000
    used = folders['/'] # total storage used can be found from the outermost folder /
    required_folder_size = min(s for s in folders.values() if (available - used) + s >= unused)
    print("Part 2:", required_folder_size)

    return 

if __name__ == "__main__":
    analyse("D7_data.txt")