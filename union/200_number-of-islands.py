
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        row = len(grid); col = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1
        
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count

# self.count 先算出所以1之和
# parent = [i for i in range(row*col)]
# 2d array 变成 1d array
# index = i*col + j
# 向右向下 找union
# xroot, yroot = find(x),find(y)
# if xroot == yroot: return 
# 如果向右向下 为 1 且 parent不同
# parent[xroot] = yroot
# self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        if (len(grid) == 0):
            return 0
        row_max = len(grid)
        col_max = len(grid[0])
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, row_max, col_max)
                    island += 1
        
        return island
    
    def dfs(self, grid, i, j,  row_max, col_max):
        if (0<= i and i<row_max and 0 <= j and j< col_max and grid[i][j] == '1'):
            grid[i][j] = '-'
            self.dfs(grid, i-1 , j , row_max, col_max)
            self.dfs(grid, i , j-1 , row_max, col_max)
            self.dfs(grid, i+1 , j , row_max, col_max)
            self.dfs(grid, i , j+1 , row_max, col_max)
        else:
            return