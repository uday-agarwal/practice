"""
Problem:
    Given an array of 1-n digits in unordered fashion.
    You can swap any two elements at a time.
    Calculate the minimum number of swaps required to sort the array.

Solution:
    Iterate through the array once.
    For each element, swap it with its right position.
    Repeat until the element at this position is correct.

Complexity: O(n) since 1 swap for each element
"""

def minimumSwaps(arr):
    swap_count = 0
    print(arr)
    for i in range(len(arr) - 1): # Last position need not be checked
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
            swap_count += 1
        print(arr)
    return swap_count

print(minimumSwaps([4,3,1,2]))
