"""Simple unweighted, undirected graph.

Example graph here is:
     A - B - E
    / \
   C   D
  / \ / \
 F   G - H
"""

from collections import deque

class Vertex:
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return str(self.data)

class Edge:
    def __init__(self, source: Vertex, dest: Vertex, weight: int = 0, directed: bool = False):
        self.source = source
        self.dest = dest
        self.weight = weight
        self.directed = directed

class Graph:
    def __init__(self):
        # Set of all Vertex objects in a graph
        self.vertices = set()

        # Key: Vertex
        # Value: set of Edge objects
        self.edges = dict()

    def insert_vertex(self, v: Vertex):
        if not self.vertices:
            self.vertices = set({v})
        else:
            self.vertices.add(v)
    
    def insert_edge(self, edge: Edge):
        if edge.source not in self.edges:
            self.edges[edge.source] = set({edge})
        else:
            self.edges[edge.source].add(edge)

        if not edge.directed:
            if edge.dest not in self.edges:
                self.edges[edge.dest] = set({Edge(edge.dest, edge.source, edge.weight)})
            else:
                self.edges[edge.dest].add(Edge(edge.dest, edge.source, edge.weight))

    def __str__(self):
        s = ''
        for vertex, edges in self.edges.items():
            s += str(vertex) + ": " + str([edge.dest.data for edge in edges]) + "\n"
        return s

    def bfs(self, starting: Vertex, query: str):
        q = deque()
        visited = set()

        q.append(starting)
        while len(q):
            v = q.popleft()
            visited.add(v)

            if v.data == query:
                return v

            for edge in self.edges[v]:
                if edge.dest not in visited:
                    q.append(edge.dest)

        return None

    def dfs(self, starting: Vertex, query: str):
        s = []
        visited = set()
        s.append(starting)

        while len(s):
            v = s.pop()
            visited.add(v)
                
            if v.data == query:
                return v
            
            for edge in self.edges[v]:
                if edge.dest not in visited:
                    s.append(edge.dest)
        
        return None

    def shortestPath(self, start: Vertex, end: Vertex):
        distance = {}
        parent = {}
        q = deque()
        discovered = set()

        if start == None or end == None:
            return None
        if start == end:
            return [start]

        q.append(start)
        distance[start] = 0
        discovered.add(start)
        parent[start] = start
        while len(q):
            v = q.popleft()

            distance[v] = min(distance[v], distance[parent[v]] + 1)

            if v == end:
                return distance[v]

            for edge in self.edges[v]:
                if edge.dest not in discovered:
                    q.append(edge.dest)
                    discovered.add(edge.dest)
                    distance[edge.dest] = distance[v] + 1
                    parent[edge.dest] = v

        return None

def main():
    g = Graph()
    vertices = []
    for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        vertex = Vertex('v' + char)
        vertices.append(vertex)
        g.insert_vertex(vertex)

    g.insert_edge(Edge(vertices[0], vertices[1]))
    g.insert_edge(Edge(vertices[0], vertices[2]))
    g.insert_edge(Edge(vertices[0], vertices[3]))
    g.insert_edge(Edge(vertices[1], vertices[4]))
    g.insert_edge(Edge(vertices[2], vertices[5]))
    g.insert_edge(Edge(vertices[2], vertices[6]))
    g.insert_edge(Edge(vertices[3], vertices[6]))
    g.insert_edge(Edge(vertices[3], vertices[7]))
    g.insert_edge(Edge(vertices[6], vertices[7]))

    if g.bfs(vertices[0], 'vC'): 
        print("Found vC via vA using BFS")
    else:
        print("Not found vC via vA using BFS")

    if g.bfs(vertices[3], 'vX'): 
        print("Found vX via vD using BFS")
    else: 
        print("Not found vX via vD using BFS")

    if g.dfs(vertices[4], 'vY'): 
        print("Found vY via vE using DFS")
    else: 
        print("Not found vY via vE using DFS")

    if g.dfs(vertices[1], 'vF'): 
        print("Found vF via vB using DFS")
    else: 
        print("Not found vF via vB using DFS")

    print("Shortest path vA to vH: ", g.shortestPath(vertices[0], vertices[7]))
    print("Shortest path vA to vD: ", g.shortestPath(vertices[0], vertices[3]))
    print("Shortest path vB to vH: ", g.shortestPath(vertices[1], vertices[7]))

if __name__ == "__main__":
    main()
