class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols, mainD, secondD = set(), set(), set()

        res = []

        def backtrack(row):
            if row == n:
                copy = ["".join(board[i]) for i in range(n)]
                res.append(copy)
                return
            for col in range(n):  
                calcMain, calcSecond = row-col, row+col
                if (col in cols or calcMain in mainD or calcSecond in secondD):
                    continue

                board[row][col] = "Q"
                cols.add(col)
                mainD.add(calcMain)
                secondD.add(calcSecond)
                 
                backtrack(row+1)

                board[row][col] = "."
                cols.remove(col)
                mainD.remove(calcMain)
                secondD.remove(calcSecond)
        
        backtrack(0)
        return res

                
