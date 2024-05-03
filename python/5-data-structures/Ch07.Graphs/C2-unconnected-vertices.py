class Graph:
    def unconnected_vertices(self):
        unconnected = []
        for vert, connects in self.graph.items():
            if not connects:
                unconnected.append(vert)
        return unconnected


    # don't touch below this line


    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_vertex(self, u):
        if u not in self.graph:
            self.graph[u] = set()



# -----------------------------------------------------------------------------



# INIT
result = Graph()
p0, p1, p2, p3, p4, p5 = 0, 1, 2, 3, 4, 5

# ADD_EDGE
print(f"Adding values to the Adjacency List:")
print(f"{p1} -> {p3}\n{p2} -> {p3}\n{p4}\n{p5}")
result.add_edge(p1, p3)
result.add_edge(p2, p3)
result.add_vertex(p4)
result.add_vertex(p5)
print("---\n")

# PRINT GRAPH
print("Graph:")
formatted_graph = "{\n"
for key in sorted(result.graph.keys()):
    formatted_graph += f'    "{key}": {result.graph[key]},\n'
formatted_graph = formatted_graph.rstrip(",\n") + "\n}"
print(formatted_graph)
print("---\n")

# ADJACENT_VERTICES
print("Unconnected Vertices")
print(result.unconnected_vertices())

