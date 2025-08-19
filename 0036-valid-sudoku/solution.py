class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = defaultdict(set), defaultdict(set)
        subbox = [[None] * 3 for i in range(3)]
        #print(subbox)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": 
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or (subbox[i//3][j//3] and board[i][j] in subbox[i//3][j//3]):
                    print(subbox)
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                if not subbox[i//3][j//3]:
                    subbox[i//3][j//3] = set()
                subbox[i//3][j//3].add(board[i][j])

        return True
