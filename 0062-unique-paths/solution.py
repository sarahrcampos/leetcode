class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        memo[m-1][n-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                memo[i][j] = 0 + (memo[i][j+1] if j+1 < n else 0) + (memo[i+1][j] if i+1 < m else 0)                
        
        return memo[0][0]
