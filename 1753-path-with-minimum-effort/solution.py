class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minEffort = [[float("inf")] * COLS for _ in range(ROWS)]
        
        minHeap = [(0, (0,0))] #= (max effort in the path, (i,j))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while minHeap:
            effort, location = heapq.heappop(minHeap)
            i, j = location
            if i == ROWS - 1 and j == COLS-1:
                return effort

            if minEffort[i][j] != float("inf"): #ja encontramos o min pra esse nó
                continue
            minEffort[i][j] = effort

            for di, dj in directions:
                newI, newJ = i + di, j + dj
                if 0<=newI<ROWS and 0<=newJ<COLS:
                    maxEffort = max(effort, abs(heights[i][j] - heights[newI][newJ]))
                    heapq.heappush(minHeap, (maxEffort, (newI, newJ)))


