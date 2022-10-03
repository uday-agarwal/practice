"""Subsets

Given a set of numbers, find all subsets of this set.

Input: {1, 3, 4}
Output: {{}, {1}, {3}, {4}, {1,3}, {1,4}, {3,4}, {1,3,4}}
"""

import copy
from typing import List

def find_subsets(l: List) -> List[List[int]]:
    output = [[]]

    for element in l:
        duplicate = copy.deepcopy(output)
        for sublist in duplicate:
            sublist.append(element)
        output.extend(duplicate)

    return output

def main():
    print(find_subsets([1, 3, 4]))

if __name__ == "__main__":
    main()
