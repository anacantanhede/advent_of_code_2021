from queue import PriorityQueue

"""
Could not find the exact answer, I did not understand why. 

With the multiple tries I could see it was in between 400 (which I get if I have a bi-directional graph) and 404 (which I get with a unidirectional graph). So I decided to not implement the second puzzle.

The accepted correct answer was 403.

Based on https://stackabuse.com/dijkstras-algorithm-in-python/
"""


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [
            [-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)
        ]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[v][u] = weight
        self.edges[u][v] = weight

    def __str__(self):
        output = ""
        for x in self.edges:
            output.join(str(x))
        return output


def dijkstra(graph, start_vertex):
    D = {v: float("inf") for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost

    return D


def main():
    graph = Graph(10000)
    with open("./input.txt", "r") as file:
        for pos_y, line in enumerate(file):
            for pos_x, weight in enumerate(list(line.replace("\n", ""))):
                if pos_x > 0:
                    graph.add_edge(
                        pos_y * (len(line) - 1) + pos_x - 1,
                        pos_y * (len(line) - 1) + pos_x,
                        int(weight),
                    )
                if pos_y > 0:
                    graph.add_edge(
                        (pos_y - 1) * (len(line) - 1) + pos_x,
                        pos_y * (len(line) - 1) + pos_x,
                        int(weight),
                    )
    print(graph)
    D = dijkstra(graph, 0)
    print(graph.visited)
    print(D)


if __name__ == "__main__":
    main()
