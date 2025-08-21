class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        left, right = 0, COLS - 1

        row = -1
        while top <= bottom:
            m = (top+bottom) // 2
            if target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][COLS-1]:
                top = m + 1
            else:
                row = m
                break
        if row == -1:
            return False

        while left <= right:
            col = (right + left) // 2
            if target < matrix[row][col]:
                right = col - 1
            elif target > matrix[row][col]:
                left = col + 1
            else:
                return True

        return False
