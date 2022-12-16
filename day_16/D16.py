#   Advent of Code 2022 - Day 16
#   Eetu Knutars / @knuutti

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

    file = open('D16_data.txt', 'r')
    data = file.read().splitlines()
    file.close()

    valve_names = {}

    index = 0
    for line in data:
        temp = line.split('=')
        valve_name = temp[0].rstrip(' has flow rate')[6:]
        valve_names[valve_name] = index
        index += 1

    valves = len(valve_names)
    flow_values = [0] * valves

    # creating the matrix
    M = []
    for i in range(len(valve_names)):
        M.append([])
        for _ in range(len(valve_names)):
            M[i].append(0)


    for line in data:        
        temp = line.split('=')
        index = valve_names[temp[0].rstrip(' has flow rate')[6:]]
        temp = temp[1].split(';')
        flow_values[index] = int(temp[0])
        temp = temp[1].split(', ')

        M[index][valve_names[temp[0][len(temp[0])-2:len(temp[0])]]] = 1

        for i in range(1, len(temp)):
            M[index][valve_names[temp[i]]] = 1

    graph = Graph(len(valve_names), M)

    

    distances = []
    for i in range(valves):
        distances.append(graph.dijkstra(i))

    ######################## ANALYSIS

    total_flow, current_flow, current_location, best = 0, 0, valve_names['AA'], valve_names['AA']
    time_remaining = 30

    best_value = flow_values[best] * 2
    for i in range(valves):
        if i == current_location:
            continue
        # finding the best location to move first before opening a valve
        flow_value = flow_values[i]/(distances[current_location][i])
        if flow_value > best_value:
            best = i
            best_value = flow_value

    time_remaining -= distances[current_location][best]   # moving to the valve
    current_location = best # updating current location

    while time_remaining > 0:
        # opening the current valve
        time_remaining -= 1
        total_flow += time_remaining*flow_values[current_location]
        flow_values[current_location] = 0 # open valve, no more extra flow available
        
        best_value = 0
        for i in range(valves):
            if i == current_location or distances[current_location][i] >= time_remaining:
                continue
            # finding the best location to move next
            flow_value = flow_values[i]/(distances[current_location][i])
            if flow_value > best_value:
                best = i
                best_value = flow_value

        if best == current_location:
            # no more optimal valves
            break

        time_remaining -= distances[current_location][best]
        current_location = best
        
    print("Part 1:", total_flow)



if __name__ == '__main__':
    main()