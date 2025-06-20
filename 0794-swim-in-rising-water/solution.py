class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] #cost, i, j
        visited = set()
        t = 0
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        while heap:
            cost, i, j = heapq.heappop(heap)
            t = max(t, cost)
            if i == n-1 and j == n-1:
                return t
            visited.add((i,j))
            for di, dj in directions:
                newi, newj = i+di, j+dj
                if newi in range(0,n) and newj in range(0,n) and (newi, newj) not in visited:
                    newcost = max(cost, grid[newi][newj])
                    heapq.heappush(heap, (newcost, newi, newj))
                    visited.add((newi,newj))
        return t
