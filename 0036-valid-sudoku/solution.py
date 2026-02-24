#subboxes
#i: 0-2         i: 0-2         i: 0-2       -> i//3 = 0
#j: 0-2         j: 3-5         j:6-8

#i: 3-5         i: 3-5         i: 3-5       -> i//3 = 1
#j: 0-2         j: 3-5         j:6-8

#i: 6-8         i: 6-8         i: 6-8       -> i//3 = 2
#j: 0-2         j: 3-5         j:6-8

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[False] * 10 for _ in range(9)]
        subbox = [[[False] * 10 for _ in range(3)] for _ in range(3)]
        for i in range(0,9):
            row = set()
            for j in range(0,9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row or cols[j][int(num)] or subbox[i//3][j//3][int(num)]:
                    return False
                row.add(num)
                cols[j][int(num)] = True
                subbox[i//3][j//3][int(num)] = True
        return True
            
