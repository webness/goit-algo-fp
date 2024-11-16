import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Remove this line for directed graphs

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        previous = {vertex: None for vertex in self.graph}
        priority_queue = [(0, start)]  # (distance, vertex)
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous

    def shortest_path(self, start, end):
        distances, previous = self.dijkstra(start)
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        return path[::-1], distances[end]


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'D', 3)
    g.add_edge('D', 'E', 1)
    g.add_edge('C', 'E', 4)

    start_vertex = 'A'
    distances, _ = g.dijkstra(start_vertex)

    print(f"Shortest distances from vertex '{start_vertex}':")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

    end_vertex = 'E'
    path, path_distance = g.shortest_path(start_vertex, end_vertex)
    print(f"\nShortest path from '{start_vertex}' to '{end_vertex}': {path}")
    print(f"Path distance: {path_distance}")
