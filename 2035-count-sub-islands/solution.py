class Solution(object):
    def countSubIslands(self, grid1, grid2):
        ROWS, COLS = len(grid2), len(grid2[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        def bfs(i, j):
            queue = deque()
            queue.append((i,j))
            subisland = True
            while queue:
                i, j = queue.popleft()
                grid2[i][j] = -1
                if grid1[i][j] == 0:
                    subisland = False
                for di, dj in directions:
                    newi, newj = i+di, j+dj
                    if newi >= 0 and newi < ROWS and newj >= 0 and newj < COLS and grid2[newi][newj] == 1:
                        queue.append((newi, newj))
                        grid2[newi][newj] = -1
            return 1 if subisland else 0
        
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1:
                    count += bfs(i,j)
        
        return count
