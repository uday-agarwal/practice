''' Cyclic sort involves swapping each out of place element with 
the element at its correct position. This way, there are at most N swaps.
So the time complexity is linear: O(n)

Question: Find the first non-negative integer outside the input array.

Input: [3, 4, 2, 5, 1, 6, 9, 0]
Sorted array: [0, 1, 2, 3, 4, 5, 6, 9]
Output: 7

'''

from typing import List

def lowest_integer_outside_array(arr: List[int]) -> int:
    # Sort first
    for index, number in enumerate(arr):
        while number < len(arr) and number != index:
            arr[index], arr[number] = arr[number], arr[index]
            number = arr[index]

    # Find the first integer outside the array
    for index, number in enumerate(arr):
        if index != number:
            return index

if __name__ == "__main__":
    print(lowest_integer_outside_array([3, 4, 2, 5, 1, 6, 9, 0]))

