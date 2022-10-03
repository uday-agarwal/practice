"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Input: s = "3z4"
Output: ["3z4","3Z4"]

1 <= s.length <= 12

Approach:

Complexity:

"""
# from curses.ascii import isalpha
from typing import List

def letterCasePermutation(s: str) -> List[str]:
    s = s.lower()
    permutations = ['']

    i = 0
    while i < 1 << len(s):
        modified = s
        for j in range(len(s)):
            if ((i >> j) & 1) == 1:
                modified = modified[0:j] + modified[j].upper() + modified[j+1:]
        permutations.add(modified)
        i += 1

    return permutations

print(letterCasePermutation("a1b2"))
print(letterCasePermutation("3z4"))