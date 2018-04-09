'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

# DFS, get '1' and check all its neighbors, mark to 0 if they are '1'
class Solution:
    def dfs_1_to_0(self, grid, i, j):
        """
        :type grid: List[List[str]], i, j
        :rtype: None
        """
        if i < 0 or i >= len(grid): return
        if j < 0 or j >= len(grid[0]): return
        if grid[i][j] == '0': return
        else:
            grid[i][j] = '0'
            self.dfs_1_to_0(grid, i-1, j)
            self.dfs_1_to_0(grid, i+1, j)
            self.dfs_1_to_0(grid, i, j-1)
            self.dfs_1_to_0(grid, i, j+1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        if len(grid) == 0:
            return islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs_1_to_0(grid, i, j)
                    islands += 1
        return islands

