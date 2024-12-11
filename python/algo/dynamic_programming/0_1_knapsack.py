"""Given N items each with weight and value, and a bag with capacity C.
Calculate maximum value of items that can be kept without exceeding capacity in weight.

Input: weights=[2, 3, 1, 4], values=[6, 8, 9, 14], capacity=6
Output: 23

Approach:
This is a DP problem. Can be solved using tabulation.
For each capacity - go item wise. Decide whether to pick item or not.

2D matrix of value for each capacity when a subset of items are picked.
Rows = items (N), Columns = knapsack capacity (C)

                        Capacity --->
Weight  Value   Items   0   1   2   3   4   5   6
  -       -     0       0   0   0   0   0   0   0
  2       6     1       0   0   6   6   6   6   6
  3       8     2       0   0   6   8   8   14  14
  1       9     3       0   9   9   15  17  17  23
  4       14    4       0   9   9   15  17  23  23

Formula:
DP[i, j] = max(  DP[i - 1, j],       V[i] + DP[i - 1, j - W[i]])
                Item not picked  v   Item picked

Complexity:
- Time: Traversing every element in matrix: O(N * C), N = number of items, C = capacity of knapsack
- Space: O(N*C)

"""

from typing import List, Tuple

def knapsack(weights: List[int], values: List[int], capacity: int) -> Tuple[int, int]:
    # Construct a DP tabulation
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    
    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            smaller_kp = 0
            if j - weights[i-1] >= 0:
                smaller_kp = dp[i - 1][j - weights[i-1]] + values[i-1]
            dp[i][j] = max(dp[i-1][j], smaller_kp)

    print(dp)
    return dp[-1][-1]

print(knapsack(weights=[2, 3, 1, 4], values=[6, 8, 9, 14], capacity=6))

