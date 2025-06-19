class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, rotten = 0, 0
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten += 1
                    queue.append((i,j))
        if not rotten and not fresh:
            return 0

        directions = [
            [1,0],
            [-1,0],
            [0,-1],
            [0,1]
        ]
        minutes = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    newi, newj = i + di, j + dj
                    if newi in range(0,ROWS) and newj in range(0,COLS) and grid[newi][newj] == 1:
                        fresh -= 1
                        grid[newi][newj] = 2
                        queue.append((newi,newj))
            minutes += 1
        
        return minutes if not fresh else -1
