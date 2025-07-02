class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        counter = [[0] * (n+1) for _ in range(m+1)]
        counter[m-1][n-1] = 1

        print(counter)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1 or obstacleGrid[i][j] == 1:
                    continue
                counter[i][j] = counter[i+1][j] + counter[i][j+1]
        print(counter)
        return counter[0][0]
