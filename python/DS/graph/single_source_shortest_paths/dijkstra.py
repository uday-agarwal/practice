''' Dijkstra's algorithm for shortest path to a node

Algorithm:
This requires a Min heap of all nodes keyed by their distance from source
Steps are:
 - Construct a min heap with just the source node
 - While the heap is non empty:
    - Pick top of heap
    - Mark this node as visited
    - For all neighbors:
        - Calculate new minimum distance from source
        - If node == target, exit
        - If there is a distance update, insert into heap

The heap would have duplicates for the same vertex - with different distances from source.
Only the lowest one would be processed and others ignored.
This way we don't have to update entries in the heap (which is a complex operation).

The approach of starting with just source code in the heap is useful in the
Uniform Cost Search method, a variant of Dijkstra.

Complexity:
    O(E + V log V) using heap and aux data structure to remember positions of each node


Graph:
    B---6---F
   / \       \
  5   1       7
 /     \       \
A---3---C---4---D---2---E

Input: source='A', target='D'
Intermediate: A: 0, B: 4, C: 3, D: 7, E: 9, F: 10
Output: 7

Another:
    B---2---C
   /       /
  8       10
 /       /
A---4---D

Input: source='A', target='C'
Intermediate: A: 0, B: 8, C: 10, D: 4
Output: 10

'''

from heapq import heappop, heappush
from typing import List, Tuple

class Graph:
    def __init__(self, adj_list) -> None:
        self.adj_list = adj_list

    def __str__(self) -> str:
        output = ''
        for node, neighbors in self.adj_list.items():
            output += node + ":" + str(neighbors) + '\n'
        return output

    def dijkstra(self, source: str, target: str) -> Tuple[int, List[str]]:
        min_distance = {}
        previous = {}
        visited = set()
        queue = []

        if source == target:
            return 0, []

        for vertex in self.adj_list:
            previous[vertex] = None
            min_distance[vertex] = float('inf')
            if vertex == source:
                min_distance[vertex] = 0
                queue.append((0, vertex))

        while queue:
            distance, node = heappop(queue)

            # Because we are keeping copies of a node in the heap
            if node in visited:
                continue
            visited.add(node)

            for neighbor, edge_weight in self.adj_list[node]:
                if neighbor in visited:
                    continue

                # If there is a distance update, insert neighbor into heap
                if distance + edge_weight < min_distance[neighbor]:
                    min_distance[neighbor] = distance + edge_weight
                    previous[neighbor] = node
                    if neighbor == target:
                        break
                    heappush(queue, (min_distance[neighbor], neighbor))

        path = []
        node = target
        while node != source:
            path.append(previous[node])
            node = previous[node]
        return min_distance[target], path[::-1]

def main():
    g1 = Graph({
            'A': [('B', 5), ('C', 3)],
            'B': [('A', 5), ('C', 1), ('F', 6)],
            'C': [('A', 3), ('B', 1), ('D', 4)],
            'D': [('C', 4), ('F', 7), ('E', 2)],
            'E': [('D', 2)],
            'F': [('B', 6), ('D', 7)]
        })
    print("Graph:")
    print(g1)
    distance, path = g1.dijkstra(source='A', target='D')
    print(distance, path)

        
    g2 = Graph({
            'A': [('B', 8), ('D', 4)],
            'B': [('A', 8), ('C', 2)],
            'C': [('B', 2), ('D', 10)],
            'D': [('A', 4), ('C', 10)],
        })
    print("Graph:")
    print(g2)
    distance, path = g2.dijkstra(source='A', target='C')
    print(distance, path)


if __name__ == "__main__":
    main()