"""Min Heap functions to work on an input array

Key points:
Given index i, left child =  2i + 1
               right child = 2i + 2
               parent = (i - 1) // 2
"""

from typing import List

class MinHeap:
    @staticmethod
    def heapify(data: List, using_siftup: bool = True):
        if not data:
            return

        if using_siftup:
            # Expand the heap from 1st element onward.
            for end in range(0, len(data)):
                test = data[0:end+1]
                MinHeap.siftUp(test) # Simply passing data[0:i+1] creates a new list, updating which doesn't reflect here.
                data[0:end+1] = test
                print(data)
        else:
            # Contract the heap from the last element downward.
            for start in range((len(data) - 2) // 2, -1, -1):
                test = data[start:len(data)]
                MinHeap.siftDown(test)
                data[start:len(data)] = test
                print(data)

    @staticmethod
    def siftUp(data: List):
        """Swap the last element with its parent if parent is larger.
        Repeat for the parent if there was a swap."""
        if not data:
            return

        index = len(data) - 1
        parent = (index - 1) // 2
        while parent >= 0:
            if data[parent] > data[index]:
                data[index], data[parent] = data[parent], data[index]
                index = parent
                parent = (index - 1) // 2
            else:
                return
            # print(data)

    @staticmethod
    def siftDown(data: List):
        """Swap the first element with the smaller of its two children.
        Repeat for each child position that is swapped out, until there
        is no more child available."""
        if not data:
            return
        
        index = 0
        while 2*index+1 < len(data):
            left_child = 2*index + 1
            right_child = 2*index + 2
            swap_with = index
            if data[swap_with] > data[left_child]:
                swap_with = left_child
            if right_child < len(data) and data[swap_with] > data[right_child]:
                swap_with = right_child
            if swap_with == index:
                return
            data[swap_with], data[index] = data[index], data[swap_with]
            index = swap_with
            # print(data)

    @staticmethod
    def insert(self, data: int):
        pass

    @staticmethod
    def pop_min(self, data: List):
        pass

    def __str__(self):
        return str(self.data)

def main():
    a = [10, 18, 8, 12, 4, 3, 11, 9, 20, 1, 2]
    print("Input:", a)
    # MinHeap.siftDown(a)
    # MinHeap.siftUp(a)
    MinHeap.heapify(a, using_siftup = True)
    # MinHeap.heapify(a, using_siftup = False)
    # print(heap)

if __name__ == "__main__":
    main()
