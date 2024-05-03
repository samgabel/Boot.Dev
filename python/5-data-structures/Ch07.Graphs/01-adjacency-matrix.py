# We want to create an Adjacency Matrix and create a method to specify an edge to the adjacency matrix



class Graph:
    def __init__(self, num_vertices):
        # our adjacency matrix will be nested arrays
        self.graph = []
        for _ in range(num_vertices):
            self.graph.append([False for _ in range(num_vertices)])
        # List comprehension of the above:
        # self.graph = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True


    # don't touch below this line


    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]


# ----------------------------------------------------------------------------



# INIT
result = Graph(5)
p1, p2 = 2, 3

# ADD_EDGE
print(f"Adding '{p1}' and '{p2}' to the Adjacency Matrix:\n")
result.add_edge(p1, p2)

# PRINT GRAPH
formatted_graph = "[\n"
for lst in result.graph:
    formatted_graph += f'    {lst},\n'
formatted_graph = formatted_graph.rstrip(",\n") + "\n]"
print(formatted_graph)


# EGDE EXISTS?
print(f"\nDo '{p1}' and '{p2}' share an edge?: {result.edge_exists(p1, p2)}")
print(f"Do '1' and '2' share an edge?: {result.edge_exists(1, 2)}")
