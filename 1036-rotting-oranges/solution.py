class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        fresh = 0
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        time = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    newI, newJ = i + di, j + dj
                    if (0 <= newI < ROWS and 0 <= newJ < COLS and grid[newI][newJ] == 1):
                        grid[newI][newJ] = 2
                        fresh -= 1
                        queue.append((newI, newJ))
            time += 1
        return max(time-1, 0) if fresh == 0 else -1
