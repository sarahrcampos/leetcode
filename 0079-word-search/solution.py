class Solution(object):
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        used = set()
        def backtrack(bi,bj,wi):
            if wi == len(word):
                return True
            if bi<0 or bi>=ROWS or bj<0 or bj>=COLS or (bi,bj) in used or board[bi][bj] != word[wi]:
                return False
            
            used.add((bi,bj))
            for di,dj in directions:
                newi, newj = bi+di, bj+dj
                if backtrack(newi, newj, wi+1):
                    return True
            used.remove((bi,bj))
            return False
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0] and backtrack(i,j,0):
                    return True
        return False
        
