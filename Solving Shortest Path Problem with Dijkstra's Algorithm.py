# Task 1: Define Graph Representation
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}


# Task 2: Implement Dijkstra's Algorithm

    def find_shortest(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# Task 3: Test the Algorithm Implementation

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)

print(graph.find_shortest('A'))
print(graph.find_shortest('B'))
print(graph.find_shortest('C'))

# Task 4: Analyze Time and Space Complexity

'''
Time Completixy is O(n^2) since we have to iterate through each node for each end destination calculation
Space Complexity is O((nk)^2) Where is the number of nodes and k is the number of edges. Potentially each node could have an edge to each other node
'''