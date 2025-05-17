class Solution(object):
    def findMaxFish(self, grid):
        ROWS, COLS, maxFish = len(grid), len(grid[0]), 0

        def bfs(i,j):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            area = 0
            queue = deque()
            queue.append([i,j])
            while queue:
                cur_i, cur_j = queue.popleft()
                area += grid[cur_i][cur_j]
                grid[cur_i][cur_j] = 0
                for di, dj in directions:
                    i, j = cur_i + di, cur_j + dj
                    if i >= 0 and i < ROWS and j >= 0 and j < COLS and grid[i][j] > 0:
                        queue.append([i,j])
                        area += grid[i][j]
                        grid[i][j] = 0
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] > 0:
                    maxFish = max(maxFish, bfs(i,j))
        
        return maxFish
        
