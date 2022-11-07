''' Given a rod of length L and a set of pieces with length and value,
find the maximum value that can be obtained after cutting the rod into
these pieces. The pieces can repeat.
Rod cutting is a variant of unbounded knapsack.

Algorithm:
 - Same as unbounded knapsack.
 - Start building the big rod from the pieces, just like filling knapsack with weights.

Complexity: 
 - Time: O(N * C) - same as unbounded knapsack
 - Space: O(C) - same as unbounded knapsack

Example:
Input: 
 L = 15
 Piece lengths: [2, 3, 6, 7]
 Piece value:   [4, 7, 11, 18]

Output: 36 since the piece length of 7 with value 18 is most efficient.

'''

from typing import List

def rod_cut_value(rod_length: int, piece_lengths: List[int], piece_values: List[int]) -> int:
    dp = [0] * (rod_length + 1)

    for i in range(rod_length + 1):
        for j in range(len(piece_lengths)):
            value_with_this_piece = 0
            if i >= piece_lengths[j]:
                value_with_this_piece = piece_values[j] + dp[i - piece_lengths[j]]
            dp[i] = max(dp[i], value_with_this_piece)

    return dp[-1]

def main():
    print(rod_cut_value(15, [2, 3, 6, 7], [4, 7, 11, 18]))

if __name__ == '__main__':
    main()