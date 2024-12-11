"""Simple unweighted, undirected graph.

Example graph here is:
     A - B - E
    / \
   C   D
  / \ / \
 F   G - H

A -> B -> E
  -> C -> F
       -> G -> H
  -> D -> G -> H
       -> H

"""

from collections import deque

class Vertex:
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return str(self.data)

class Edge:
    def __init__(self, source: Vertex, dest: Vertex, weight: int = 0, directed: bool = True):
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

    def topsort_dfs(self):
        """This code is buggy and needs work.
        """
        print("Topological sort:", end=' ')
        reversed_list = []
        stack = []
        visited_vertices = set()

        for vertex in self.vertices:
            if vertex not in visited_vertices:
                stack.append(vertex)
            while stack:
                node = stack[-1]
                if node in self.edges:
                    for edge in self.edges[node]:
                        if edge.dest not in visited_vertices:
                            stack.append(edge.dest)
                            visited_vertices.add(edge.dest)
                node = stack.pop()
                visited_vertices.add(node)
                reversed_list.append(node.data)

        print(reversed_list[::-1])

    def topsort_kahn(self):
        pass

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

    g.topsort_dfs()

if __name__ == "__main__":
    main()
