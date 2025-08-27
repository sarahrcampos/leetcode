class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        def dfs(i, j):
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                grid[i][j] != 1):
                return 0
            grid[i][j] = -1
            area = 1
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                area += dfs(newI, newJ)            
            return area

        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i,j))

        return maxArea
