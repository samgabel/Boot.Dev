# We want to be able to find the shortest path from start to end vertex in a graph.

# We assume that the end vertex is not too deeply nested from the start vertex. (so we use BFS)
# We want to return a list of all the vertices from start to end, in that order.



class Graph:
    def bfs_path(self, start, end):

    # We should verify if our inputs are legitimate

        if start not in self.graph:
            raise KeyError("Start vertex not in graph")
        if end not in self.graph:
            raise KeyError("End vertex not in graph")

    # Finding the end vertex in the graph

        # we want to create a hash table where the neighbor(keys) point to their
        # common adjacent vertex(value) for each layer of the graph
        visited = {}
        to_visit = [start]

        # we will end the loop once we found the first layer
        # where there is a vertex that contains our end in the graph
        while end not in visited:
            current_vertex = to_visit.pop(0)
            neighbors = sorted(self.graph[current_vertex])

            # append newly discoverd vertices to the enqueue and
            # make neighbor(key) -> current_vertex(pair) links
            for neighbor in neighbors:
                if neighbor not in to_visit and neighbor not in visited:
                    to_visit.append(neighbor)
                    visited[neighbor] = current_vertex

            # if we exhausted our queue then that means there is no connection
            if not to_visit:
                return None

    # Creating the path from end to start (but inserting start -> end)

        path = []
        city = end
        while start not in path:
            path.append(city)
            city = visited[city]
        # instead of inserting each vertex to the front, we want to just reverse at the end
        # because `reverse()` and `insert()` are both O(n) and we only have to invkoke `reverse()` once
        path.reverse()
        return path


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
stop = "Dubai"

print(f"The path from '{start}' -> '{stop}' using BFS is:\n")
print(graph.bfs_path(start, stop))

