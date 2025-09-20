class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = [matrix[0][0]]
        matrix[0][0] = float("-inf")
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        i = j = d = 0
        while len(res) < m*n:
            di, dj = directions[d]
            while 0 <= (i+di) <  m and 0 <= (j+dj) < n and matrix[i+di][j+dj] != float("-inf"):
                i, j = i+di, j+dj
                res.append(matrix[i][j])
                matrix[i][j] = float("-inf")
            d = (d+1)%len(directions)
        return res
