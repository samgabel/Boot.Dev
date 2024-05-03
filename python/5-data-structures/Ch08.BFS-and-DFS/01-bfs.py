class Graph:
    def breadth_first_search(self, v):
        # want to initialize with our starting vertex
        visited = []
        to_visit = [v]
        # run while there are still vertices left in to visit
        while to_visit:
            # current vertex at the head of our queue
            current_vertex = to_visit.pop(0)
            # take our vertex from the queue and "visit" it
            visited.append(current_vertex)
            # we now want to find which vertices (connected by edge to our recently visited vertex) to add to the queue
            neighbors = sorted(self.graph[current_vertex]) # 'sorted' function is just for consistency when dealing with sets
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited


    # don't touch below this line


    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result



# --------------------------------------------------------------------------



graph = Graph()

graph.add_edge("New York", "London")
graph.add_edge("New York", "Cairo")
graph.add_edge("New York", "Tokyo")
graph.add_edge("Tokyo", "Dubai")
graph.add_edge("London", "Dubai")

print( """Graph:\n
New York ---- London
   | \\          |
   |  \\         |
   |   \\       Dubai
   |    \\       |
  Cairo  \\ ___ Tokyo
\n""" )

start = "New York"

print(f"The BFS of this graph, with '{start}' as the starting point is:\n")
print(graph.breadth_first_search(start))

