class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}

        for i in range(3, 10, 3):
            for j in range(3, 10, 3):
                subbox = set()
                for si in range(i-3, i):
                    for sj in range(j-3, j):
                        if board[si][sj] == ".":
                            continue
                        if si in row and board[si][sj] in row[si]:
                            return False
                        if sj in column and board[si][sj] in column[sj]:
                            return False
                        if board[si][sj] in subbox:
                            return False

                        if si not in row:
                            row[si] = set()
                        row[si].add(board[si][sj])
                        if sj not in column:
                            column[sj] = set()
                        column[sj].add(board[si][sj])
                        subbox.add(board[si][sj])
        
        return True
                
