class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = max(grid[ROWS-1][COLS-1], grid[0][0]) #tempo mínimo pra chegar no destino saindo de 0,0

        minHeap = [[time, 0, 0]]
        visited = set([(0, 0)])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minHeap:
            time, i, j = heapq.heappop(minHeap)
            if i == ROWS-1 and j == COLS-1:
                return time
            for di, dj in directions:
                newI, newJ = i+di, j+dj
                if (0<=newI<ROWS and 0<=newJ<COLS and (newI, newJ) not in visited):
                    visited.add((newI, newJ))
                    heapq.heappush(minHeap, [max(time, grid[newI][newJ]), newI, newJ])
        return time



