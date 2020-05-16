# 64. Minimum Path Sum
# Medium

# 2675

# 55

# Add to List

# Share
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i - 1]
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 0 <= i - 1 and 0 <= j - 1:
                    grid[i][j] = min(grid[i][j - 1],
                                     grid[i - 1][j]) + grid[i][j]
                elif 0 > j - 1 and 0 <= i - 1:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                elif 0 > i - 1 and 0 <= j - 1:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                else:
                    grid[i][j] = grid[i][j]
        return grid[-1][-1]
