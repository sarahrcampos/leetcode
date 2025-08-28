class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(queue, ocean):
            while queue:
                i, j = queue.popleft()
                ocean.add((i,j))
                for di, dj in directions:
                    newI, newJ = i + di, j + dj
                    if (0 <= newI < ROWS and 
                        0 <= newJ < COLS and 
                        (newI, newJ) not in ocean and
                        heights[newI][newJ] >= heights[i][j]):
                        ocean.add((newI,newJ))
                        queue.append((newI, newJ))
            return ocean
        
        atlantic, pacific = deque(), deque()
        for j in range(COLS): 
            pacific.append((0, j))
            atlantic.append((ROWS-1, j))
        for i in range(ROWS):
            pacific.append((i, 0))
            atlantic.append((i, COLS-1))
        
        canReachAtlantic = bfs(atlantic, set())
        canReachPacific = bfs(pacific, set())

        res = []
        for i, j in canReachAtlantic:
            if (i, j) in canReachPacific:
                res.append([i, j])
        return res

