#   Advent of Code 2022 - Day 12
#   Eetu Knutars / @knuutti

# Note to self: Read the task description... entirely.

# Structure for the class Graph and Dijkstra's algorithm implemented 
# from GeeksforGeeks
class Graph():
 
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph
 
    # Function for finding the next vertex to iterate
    def minDistance(self, dist, sptSet):
 
        min = 10000000
 
        # Finding the nearest vertex which is not in the tree already
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implementing Dijkstra's algorithm
    def dijkstra(self, start):
 
        dist = [1000000] * self.V

        # Distance to the start vertex is 0
        dist[start] = 0 
        sptSet = [False] * self.V
 
        for _ in range(self.V):
 
            # Pick the minimum distance vertex which is 
            # not in the shortest path tree
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in 
            # the shortest path tree
            sptSet[u] = True
 
            # Update distance of the adjacent vertices which are 
            # not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        # Returning a list containing the minimum distances of each vertex
        return dist
    
def main():

    file_name = "d12_data.txt"
    file = open(file_name, 'r')
    data = file.read().splitlines()
    file.close()

    height = len(data)
    width = len(data[0])

    vertex_count = height * width

    M = []
    for i in range(vertex_count):
        M.append([])
        for j in range(vertex_count):
            M[i].append(0)

    start_loc = None
    end_loc = None
    a_locs = []

    # Replacing the START and END points with proper level character
    # and storing their coordinates (index value)
    for y in range(0, height): 
        for x in range(0, width):

            if data[y][x] == "S":
                start_loc = x + y*width
                a_locs.append(x + y*width)
                data[y] = data[y].replace("S", "a")

            elif data[y][x] == "E":
                end_loc = x + y*width
                data[y] = data[y].replace("E", "z")

            # Storing the location with elevation "a" (Part 2)
            elif data[y][x] == "a":
                a_locs.append(x + y*width)

    # Creating the graph matrix
    for y in range(0, height): 
        for x in range(0, width): 

            # Calculating the elevation by converting the 
            # character to it's ASCII value
            level = ord(data[y][x])

            # Checking if neighbour verteces can be visited
            if x > 0:
                # West
                if ord(data[y][x-1]) - level > -2:
                    M[x + y * width][x-1 + y * width] = 1
            if y > 0:
                # North
                if ord(data[y-1][x]) - level > -2:
                    M[x + y * width][x + (y-1) * width] = 1
            if x < width - 1:
                # East
                if ord(data[y][x+1]) - level > -2:
                    M[x + y * width][x+1 + y * width] = 1
            if y < height - 1:
                # South
                if ord(data[y+1][x]) - level > -2:
                    M[x + y * width][x + (y+1) * width] = 1

            # A vertex can be visited, if it's elevation is higher, equal
            # or 1 level lower than the current vertex's elevation

    # Creating the graph object
    graph = Graph(vertex_count, M)

    # Starting from the end location, calculate the shortest distances to
    # all other verteces
    dist = graph.dijkstra(end_loc)  

    # Distance to the start location
    print("Part 1:", dist[start_loc])

    # Finding the shortest distance from elevation "a"
    min = 100000
    for i in a_locs:
        if dist[i] < min:
            min = dist[i]

    print("Part 2:", min)

    return



if __name__ == "__main__":
    main()  