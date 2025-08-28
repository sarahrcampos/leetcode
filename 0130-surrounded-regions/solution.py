class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #mark edges
        def dfs(i, j):
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                board[i][j] != "O"):
                return
            board[i][j] = "Z"
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                dfs(newI, newJ)
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS-1)
        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS-1, j)
        
        #capture remaining
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z": #remark edges
                    board[i][j] = "O"
        
