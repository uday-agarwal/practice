''' Count sort

Assumptions:
 - The inputs are between a fixed range, say 0 - k, i.e. k is the maximum input

Algorithm:
1. Create a new array of length k+1 (from 0 to k index) initialized to zeros
2. Run through the input array and count occurrence of each number
3. Run through the count array:
  - As long as count > 0:
    - Add the index of count array to output array
    - Decrease the count

CLRS has a different method to keep this sort stable. My method is unstable sort.

Complexity: O(n)

Input: [5, 6, 3, 8, 3, 2, 0],
       8 (max number in input array)
Output: [0, 2, 3, 3, 5, 6, 8]
'''

from typing import List

def count_sort(arr: List[int], max: int) -> List[int]:
    aux = [0 for _ in range(max+1)]

    for item in arr:
        aux[item] += 1

    # This is unstable, but count sort is a stable sort
    # A different approach is in CLRS page 195
    output = []
    for i in range(max+1):
        while aux[i] > 0:
            output.append(i)
            aux[i] -= 1

    return output

if __name__ == '__main__':
    print(count_sort([5, 6, 3, 8, 3, 2, 0], 9))
