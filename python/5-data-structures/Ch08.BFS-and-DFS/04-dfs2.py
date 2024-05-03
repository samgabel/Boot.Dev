# This is an implementation of DFS traversal using a while loop instead of recursive helper method

# In this method we make use of the stack to keep track of our traversal



class Graph:
    def depth_first_search(self, starting_vertex):
        visited = []
        to_visit = [starting_vertex]
        while to_visit:
            current_vertex = to_visit.pop()
            if current_vertex not in visited:
                visited.append(current_vertex)
                neighbors = sorted(self.graph[current_vertex])
                for neighbor in neighbors:
                    if neighbor not in visited:
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

print(f"The DFS of this graph, with '{start}' as the starting point is:\n")
print(graph.depth_first_search(start))


