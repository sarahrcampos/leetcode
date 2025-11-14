class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        maxSide = 0

        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if matrix[i][j] == "0":
                    continue
                right = int(matrix[i][j+1]) if j+1 < COLS else 0
                bottom = int(matrix[i+1][j]) if i+1 < ROWS else 0
                diagonal = int(matrix[i+1][j+1]) if i+1 < ROWS and j+1 < COLS else 0

                side = 1 + min(right, bottom, diagonal)
                maxSide = max(maxSide, side)
                matrix[i][j] = str(side)
        
        return maxSide**2

