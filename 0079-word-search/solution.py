class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def backtrack(wi, visited, i, j):
            if (i,j) in visited or board[i][j] != word[wi]:
                return False
            if wi == len(word)-1:
                return True
            
            
            visited.add((i,j))
            for di, dj in directions:
                newI, newJ = i+di, j+dj
                if 0 <= newI < len(board) and 0 <= newJ < len(board[0]) and (newI, newJ) not in visited:
                    if backtrack(wi+1, visited, newI, newJ):
                        return True
            visited.remove((i,j))

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(0,set(),i,j):
                    return True

        return False
