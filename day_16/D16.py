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

    def maxDistance(self, dist, sptSet):
 
        max = -10000000
 
        # Finding the nearest vertex which is not in the tree already
        for v in range(self.V):
            if dist[v] > max and sptSet[v] == False:
                max = dist[v]
                max_index = v
 
        return max_index
 
    # Function that implementing Dijkstra's algorithm
    def dijkstra(self, start):
 
        dist = [-1000000] * self.V

        # Distance to the start vertex is 0
        dist[start] = 0 
        sptSet = [False] * self.V
 
        for _ in range(self.V):
 
            # Pick the minimum distance vertex which is 
            # not in the shortest path tree
            u = self.maxDistance(dist, sptSet)
 
            # Put the minimum distance vertex in 
            # the shortest path tree
            sptSet[u] = True
 
            # Update distance of the adjacent vertices which are 
            # not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] < dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        # Returning a list containing the minimum distances of each vertex
        return dist

def main():

    file = open('D16_example.txt', 'r')
    data = file.read().splitlines()
    file.close()

    valve_names = {}

    index = 0
    for line in data:
        temp = line.split('=')
        valve_name = temp[0].rstrip(' has flow rate').lstrip('Valve ')
        valve_names[valve_name] = index
        index += 1

    # creating the matrix
    M = []
    for i in range(len(valve_names)):
        M.append([])
        for _ in range(len(valve_names)):
            M[i].append(0)


    for line in data:        
        temp = line.split('=')
        index = valve_names[temp[0].rstrip(' has flow rate').lstrip('Valve ')]
        temp = temp[1].split(';')
        flow = int(temp[0])
        temp = temp[1].split(', ')

        M[index][valve_names[temp[0][len(temp[0])-2:len(temp[0])]]] = flow + 1

        for i in range(1, len(temp)):
            M[index][valve_names[temp[i]]] = flow + 1


    print(M)

    graph = Graph(len(valve_names), M)

    dist = graph.dijkstra(0)  
    print(dist)






if __name__ == '__main__':
    main()