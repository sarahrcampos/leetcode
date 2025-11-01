class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        minHeap = [(grid[0][0],0,0)]
        while minHeap:
            weight, i, j = heapq.heappop(minHeap)
            if (i, j) in visited:
                continue
            visited.add((i,j))
            if i == ROWS-1 and j == COLS - 1:
                return weight
            if i+1 < ROWS:
                heapq.heappush(minHeap, (weight + grid[i+1][j], i+1, j))
            if j + 1 < COLS:
                heapq.heappush(minHeap, (weight + grid[i][j+1], i, j + 1))
        

