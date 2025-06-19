class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0]:
            return -1
        directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

        visited = set([(0,0)])
        queue = deque([(0,0)])
        length = 1
        while queue:
            for x in range(len(queue)):
                i, j = queue.popleft()
                if i == ROWS - 1 and j == COLS - 1:
                    return length
                
                for di, dj in directions:
                    newi, newj = i + di, j + dj
                    if newi in range(0, ROWS) and newj in range(0,COLS) and (newi, newj) not in visited and grid[newi][newj] == 0:
                        visited.add((newi,newj))
                        queue.append((newi,newj))
            length += 1
        
        return -1
                
#[0,0,0]
#[1,1,0]
#[1,1,1]
