class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[1] * (COLS) for _ in range(ROWS)]
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        maxLength = 1
        def dfs(i, j):
            if cache[i][j] > 1:
                return cache[i][j]
            if i >= ROWS or j >= COLS:
                return 0
            
            for di, dj in directions:
                newI, newJ = i+di, j+dj
                if 0 <= newI < ROWS and 0 <= newJ < COLS and matrix[newI][newJ] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(newI,newJ) + 1)
            return cache[i][j]

        for i in range(ROWS):
            for j in range(COLS):
                maxLength = max(maxLength, dfs(i, j))
        return maxLength
