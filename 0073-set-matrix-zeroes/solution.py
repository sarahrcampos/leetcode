class Solution(object):
    #Time: O(n)
    #Space: O(n)
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in range(ROWS):
            for j in range(COLS):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

    

        
