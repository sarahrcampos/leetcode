class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            matrix[row] = [0] * COLS
        for col in cols:
            for i in range(ROWS):
                matrix[i][col] = 0

        
        
        #O(n³):
        # def setInf(row, col):
        #     for i in range(ROWS):
        #         if matrix[i][col] != 0 and matrix[i][col] != float("inf"):
        #             matrix[i][col] = float("inf")
        #     for j in range(COLS):
        #         if matrix[row][j] != 0 and matrix[row][j] != float("inf"):
        #             matrix[row][j] = float("inf")
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 0:
        #             setInf(i, j)
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == float("inf"):
        #             matrix[i][j] = 0



    
        
