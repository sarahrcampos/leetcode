class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        #visited = set()
        def dfs(i,j):
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                grid[i][j] != "1"):
                return
            
            grid[i][j] = "-1"
            for di, dj in directions:
                newI, newJ = i+di, j+dj
                dfs(newI, newJ)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands
