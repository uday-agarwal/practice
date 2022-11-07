"""Kruskal uses Disjoint Set (union find) DS.

Algorithm:
 - Sort all edges by their weight
 - Initialize a disjoint set - one set for each vertex
 - Initialize a selected_edge_count = 0
 - Pick the lowest edge and check if find(vertice 1) != find(vertice 2)
 - Perform union of those two vertices.
 - Insert edge into final graph (which would be the MST)
 - Repeat until N-1 edges picked

Complexity:
 - Compiling all edges: O(E)
 - Sorting edges: O(E logE)
 - Constructing the MST: O(E alpha(V)) = ~O(E)
 - Overall = O(E logE)

Input:
A---5---B--6--F 
 \     /     /
  3   1     7
   \ /     /
    C--4--D--2--E

Output:
A       B--6--F 
 \     /     
  3   1     
   \ /     
    C--4--D--2--E

"""

from typing import List, Tuple

class DisjointSet:
    def __init__(self):
        self.leaders = {}
        self.ranks = {}

    def create_set(self, node: str) -> None:
        self.leaders[node] = node
        self.ranks[node] = 1
    
    def union(self, x: str, y: str) -> None:
        """Combine two elements in one set by making leader of
        one set to be the leader of the other set.
        The set with the larger rank becomes the parent of the 
        other set.
        """
        leader_of_x = self.find(x)
        leader_of_y = self.find(y)
        if leader_of_x == leader_of_y:
            return

        if self.ranks[leader_of_x] > self.ranks[leader_of_y]:
            leader_of_y, leader_of_x = leader_of_x, leader_of_y
        
        # X has lower rank than Y
        self.leaders[leader_of_x] = leader_of_y

        # Update rank of the expanded set
        self.ranks[leader_of_y] = self.ranks[leader_of_x] + \
                                  self.ranks[leader_of_y]
        self.ranks[leader_of_x] = 0
        print(self.ranks)

    def find(self, element: str) -> str:
        """Find the leader of an element 
        
        1. If it is the element itself, return that.
        2. If not, find the leader and flatten the tree such that
           this element points to the leader directly.
        """
        if self.leaders[element] != element:
            leader = self.find(self.leaders[element])
            self.leaders[element] = leader
            return leader
        
        return element

class Graph:
    def __init__(self) -> None:
        self.adj_list = {
            'A': [('B', 5), ('C', 3)],
            'B': [('A', 5), ('C', 1), ('F', 6)],
            'C': [('A', 3), ('B', 1), ('D', 4)],
            'D': [('C', 4), ('F', 7), ('E', 2)],
            'E': [('D', 2)],
            'F': [('B', 6), ('D', 7)]
        }

    def find_edges(self) -> List[Tuple[Tuple[str, str], int]]:
        # Key: Tuple(A, B)
        # Value: weight
        edges = dict()

        for node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                edge1 = (node, neighbor[0])
                edge2 = (neighbor[0], node)
                if edge1 not in edges and edge2 not in edges:
                    edges[edge1] = neighbor[1]

        # Sorting dictionary by value
        sorted_edges = sorted(edges.items(), key=lambda item: item[1])
        print('Sorted edges:', sorted_edges)
        return sorted_edges

    def generate_mst(self) -> None:
        sorted_edges = self.find_edges()
        mst_edge_count = 0

        # Key: Vertex
        # Value: Map of (Key: Neighbor Vertex, Value: Edge Weight)
        self.mst = {}

        # Create a new disjoint set
        dj = DisjointSet()
        for node in self.adj_list:
            dj.create_set(node)

        # For each edge seen, find and union these sets
        for edge in sorted_edges:
            nodes = edge[0]
            weight = edge[1]
            if dj.find(nodes[0]) != dj.find(nodes[1]):
                # These two vertices aren't yet connected (directly or indirectly)
                # First do a union of both sets
                dj.union(nodes[0], nodes[1])

                # Insert both vertices in the MST's adjacency list
                if nodes[0] not in self.mst:
                    self.mst[nodes[0]] = {nodes[1]: weight}
                else:
                    self.mst[nodes[0]][nodes[1]] = weight
                if nodes[1] not in self.mst:
                    self.mst[nodes[1]] = {nodes[0]: weight}
                else:
                    self.mst[nodes[1]] |= {nodes[0]: weight}
                mst_edge_count += 1

            if mst_edge_count == len(self.adj_list) - 1:
                break

    def __str__(self) -> str:
        output = ''
        for node, neighbors in self.adj_list.items():
            output += node + ":" + str(neighbors) + '\n'
        return output

    def get_mst(self) -> str:
        output = ''
        for node, neighbors in self.mst.items():
            output += node + ":" + str(neighbors) + '\n'
        return output

def main():
    g = Graph()
    print("Graph:")
    print(g)
    g.generate_mst()
    print("MST:")
    print(g.get_mst())

if __name__ == "__main__":
    main()
