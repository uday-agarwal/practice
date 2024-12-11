"""Find the median of a number stream.

Infinite numbers incoming - find ongoing median of the stream.

https://leetcode.com/problems/find-median-from-data-stream/

Approach:
Two heaps: A max heap of all numbers less than median.
           A min heap of all numbers more than median.

Keep the size of both heaps same (difference of 1 at the most)

Complexity:
 - Time: 
     - Heap creation: O(n log n)
 - Space:
     - Heap length: O(n)
"""

from heapq import heappush, heappop

class Median:
    def __init__(self) -> None:
        self.left = []   # Max heap
        self.right = []  # Min heap
        self.median = None

    def add_num(self, i: int) -> None:
        if self.median == None or i < self.median:
            heappush(self.left, -i)
        else:
            heappush(self.right, i)

        if len(self.left) > len(self.right) + 1:
            heappush(self.right, -heappop(self.left))
        elif len(self.left) + 1 < len(self.right):
            heappush(self.left, -heappop(self.right))

        if len(self.left) == len(self.right):
            self.median = (-self.left[0] + self.right[0] ) / 2
        elif len(self.left) > len(self.right):
            self.median = -self.left[0]
        else:
            self.median = self.right[0]

        print(f"Inserted: {i}, Left: {self.left}, Right: {self.right}, Median: {self.median}")

def main():
    obj = Median()
    input = [5, 7, 2, 8, 1, 4, 3, 9, 20, 14, 5, 2, 9, 11]
    for i in input:
        obj.add_num(i)

if __name__ == "__main__":
    main()
