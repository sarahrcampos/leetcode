class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for j in range(COLS):
            for i in range(ROWS):
                if matrix[i][j] == 1 and i - 1 >= 0:
                    matrix[i][j] += matrix[i-1][j]
        
        maxArea = 0
        for i in range(ROWS):
            matrix[i].sort(reverse=True)
            for j in range(COLS):
                maxArea = max(maxArea, matrix[i][j], matrix[i][j] * (j + 1))
        
        return maxArea


