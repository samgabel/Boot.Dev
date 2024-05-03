class Graph:
    def adjacent_vertices(self, vertex):
        return list(self.graph[vertex])


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



# -----------------------------------------------------------------------------



# INIT
result = Graph()
p0, p1, p2, p3 = 0, 1, 2, 3

# ADD_EDGE
print(f"Adding values to the Adjacency List:")
print(f"{p0} -> {p1}\n{p0} -> {p2}\n{p1} -> {p3}\n{p2} -> {p3}")
result.add_edge(p0, p1)
result.add_edge(p0, p2)
result.add_edge(p1, p3)
result.add_edge(p2, p3)
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
print("Adjacent Vertices:")
print(f"{p1} -> {result.adjacent_vertices(p1)}")
print(f"{p3} -> {result.adjacent_vertices(p3)}")

