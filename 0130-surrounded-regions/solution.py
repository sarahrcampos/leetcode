class Solution(object):
    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        edge = set()

        def bfs(i, j):
            queue = deque()
            queue.append((i,j))
            edge.add((i,j))
            while queue:
                i, j = queue.popleft()
                for di, dj in directions:
                    newi, newj = i+di, j+dj
                    if newi>=0 and newi<ROWS and newj>=0 and newj<COLS and board[newi][newj] == "O" and (newi,newj) not in edge:
                        edge.add((newi,newj))
                        queue.append((newi,newj))        

        for i in range(ROWS):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][COLS-1] == "O":
                bfs(i, COLS-1)
        
        for j in range(COLS):
            if board[0][j] == "O":
                bfs(0,j)
            if board[ROWS-1][j] == "O":
                bfs(ROWS-1, j)
        
        for i in range(1,ROWS-1):
            for j in range(1, COLS-1):
                if board[i][j] == "O" and (i,j) not in edge:
                    board[i][j] = "X"
        
