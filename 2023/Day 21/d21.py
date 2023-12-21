class Solution():
    def __init__(self, N, data):
        self.grid = data
        self.R = len(data)
        self.C = len(data[0])
        self.visited = {}
        self.start = self.get_start()
        self.positions = self.get_positions(N, self.start)

    def get_start(self):
        for r in range(self.R):
            for c in range(self.C):
                if self.grid[r][c] == "S":
                    return [r,c]
                
    def get_positions(self, N, location):
        if N == 0:
            return [str(location)]
        
        if str(location) not in self.visited:
            self.visited[str(location)] = [N]
        elif N in self.visited[str(location)]:
            return []
        else: self.visited[str(location)].append(N)

        locations = []
        if location[0] > 0:
            if self.grid[location[0]-1][location[1]] != "#":
                locations.extend(self.get_positions(N-1, [location[0]-1,location[1]]))
        if location[0] < self.R-1:
            if self.grid[location[0]+1][location[1]] != "#":
                locations.extend(self.get_positions(N-1, [location[0]+1,location[1]]))
        if location[1] < self.C-1:
            if self.grid[location[0]][location[1]+1] != "#":
                locations.extend(self.get_positions(N-1, [location[0],location[1]+1]))
        if location[1] > 0:
            if self.grid[location[0]][location[1]-1] != "#":
                locations.extend(self.get_positions(N-1, [location[0],location[1]-1]))

        return list(dict.fromkeys(locations))



def main():
    fname = "./2023/Day 21/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    file.close()

    N = 64

    s = Solution(N, data)
    print("Part 1:", len(s.positions))
    


if __name__ == '__main__':
    main()