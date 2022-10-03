"""Calculate kth number in an array when sorted in ascending order

Approach:
Since kth smallest is needed:
    Create a k-max heap
    Insert new number if it is less than top of heap
    After traversing all elements, top of heap is answer.

Another approach:
    Create a (n-k+1) min heap
    Insert new number if it is larger than top of heap
    Top of heap is answer.

Complexity:
    O(n log k)
"""

from heapq import heapify, heappushpop
from typing import List

class MaxHeapInt(int):
    def __lt__(self, other: int) -> bool:
        return super().__gt__(other)

def find_kth_number(arr: List, k: int) -> int:
    max_heap = [MaxHeapInt(i) for i in arr[0:k]]
    heapify(max_heap)

    for item in arr[k:]:
        if item > max_heap[0]:
            heappushpop(max_heap, MaxHeapInt(item))

    return max_heap[0]


print(find_kth_number([3, 9, 4, 6, 7, 1, 5, 2, 8, 34], 4)) # => 4
print(find_kth_number([10, 23, 34, 51, 26, 45, 29, 37, 12, 5], 7)) # => 34
