class Solution(object):
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def bfs(i, j):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            area = 0
            queue = deque()
            queue.append([i,j])
            while queue:
                cur_i, cur_j = queue.popleft()
                grid[cur_i][cur_j] = -1
                area += 1
                for di,dj in directions:
                    i, j = cur_i+di, cur_j+dj
                    if i >= 0 and i < ROWS and j >= 0 and j < COLS and grid[i][j] == 1:
                        queue.append([i,j])
                        grid[i][j] = -1
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i,j))
        
        return maxArea
