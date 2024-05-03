# This method (and helper method) should find all the vertices in the graph in a DFS traversal way



class Graph:
    def depth_first_search(self, start_vertex):
        # we want a visited list that will retain values outside of recursive calls, so we create a recursive "helper" function
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        # recursively drill down where the each visited node's neighbor (that isn't in visited already) gets it's own recursive call
        for neighbor in neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)


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

print(f"The DFS of this graph, with '{start}' as the starting point is:\n")
print(graph.depth_first_search(start))

