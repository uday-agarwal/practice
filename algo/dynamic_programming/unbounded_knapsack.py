"""Unbounded knapsack.
A given item can be picked any number of times.

Input: weights=[2, 3, 2, 4], values=[6, 8, 4, 14], capacity=6
Output: 20

Approach:


Complexity:


"""

from typing import List, Tuple

def unbounded_knapsack(weights: List[int], values: List[int], capacity: int) -> Tuple[int, int]:
    dp = [0 for _ in range(capacity+1)]

    for i in range(1, capacity+1):
        for j in range(len(weights)):
            smaller_knapsack = 0
            if i - weights[j] >= 0:
                smaller_knapsack = values[j] + dp[i-weights[j]]
            dp[i] = max(dp[i], smaller_knapsack)

    print(dp)
    return dp[-1]

print(unbounded_knapsack(weights=[2, 3, 2, 4], values=[6, 8, 4, 14], capacity=6))
