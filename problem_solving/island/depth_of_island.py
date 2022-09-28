"""Given an island, find the maximum distance of land from water.

Example:
0 0 0 0 0 0 0
0 0 1 1 1 0 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0

Output: 3 (the middle 1 at 3,3)

Approach:
 - Need a queue with nulls entered. Each section of queue before a null
   represents a unit distance from sea.
 - Start with 0s and insert nearest 1 into the queue, so that the boundary 
   of each island is covered. Insert a null entry then.
 - Then process 1s in queue and insert neighbor (unvisited) 1s, followed by a null.
 - For each null seen, increment max distance by 1.
"""

from collections import deque
from typing import List

def depth_of_island(area: List[List[int]]) -> int:
    max_distance = 0

    # Elements: Tuple(row, column)
    discovered = set()

    # Queue of elements to be processed
    to_process = deque()

    for row in range(len(area)):
        for col in range(len(area[0])):
            value = area[row][col]
            if value == 0:
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                neighbors = [(x, y) for (x,y) in neighbors if x >= 0 and x < len(area) and y >= 0 and y < len(area[0])]
                for neighbor in neighbors:
                    if area[neighbor[0]][neighbor[1]] == 1 and (neighbor[0], neighbor[1]) not in discovered:
                        to_process.append((neighbor[0], neighbor[1]))
                        discovered.add((neighbor[0], neighbor[1]))

    to_process.append((None, None))

    while to_process:
        element = to_process.popleft()
        if element == (None, None):
            max_distance += 1
            if len(to_process):
                to_process.append((None, None))
        else:
            row, col = element[0], element[1]
            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            neighbors = [(x, y) for (x,y) in neighbors if x >= 0 and x < len(area) and y >= 0 and y < len(area[0])]
            for neighbor in neighbors:
                if area[neighbor[0]][neighbor[1]] == 1 and (neighbor[0], neighbor[1]) not in discovered:
                    to_process.append((neighbor[0], neighbor[1]))
                    discovered.add((neighbor[0], neighbor[1]))

    return max_distance

max_depth = depth_of_island(
    [
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 1, 1, 1, 1, 1, 0], 
        [0, 1, 1, 1, 1, 1, 0], 
        [0, 1, 1, 1, 1, 1, 0], 
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0] 
    ])

max_depth2 = depth_of_island(
    [
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0] 
    ])

max_depth3 = depth_of_island(
    [
        [0, 0, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0] 
    ])

print(max_depth)
print(max_depth2)
print(max_depth3)
