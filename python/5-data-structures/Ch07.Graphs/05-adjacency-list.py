# We want to create an Adjacency List and create a method to specify an edge to the adjacency list



class Graph:
    def __init__(self):
        # our adjacency list will be a hash table
        self.graph = {}

    def add_edge(self, u, v):
        # if u exists in the adjacency list, we add v to the set of edge vertices
        # otherwise we initialize a new set for u where v is the first vertex of the set
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v} # a dictionary with 1 value is a set
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}


    # don't touch below this line


    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False



# ---------------------------------------------------------------------



# INIT
result = Graph()
p1, p2, p3 = 2, 3, 4

# ADD_EDGE
print(f"Adding '{p1}' and '{p2}' to the Adjacency List:")
result.add_edge(p1, p2)
print(f"Adding '{p2}' and '{p3}' to the Adjacency List:\n")
result.add_edge(p2, p3)

# PRINT GRAPH
formatted_graph = "{\n"
for key in sorted(result.graph.keys()):
    formatted_graph += f'    "{key}": {result.graph[key]},\n'
formatted_graph = formatted_graph.rstrip(",\n") + "\n}"
print(formatted_graph)

# EGDE EXISTS?
print(f"\nDo '{p1}' and '{p2}' share an edge?: {result.edge_exists(p1, p2)}")
print(f"Do '{p1}' and '{p3}' share an edge?: {result.edge_exists(p1, p3)}")

