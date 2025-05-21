class Solution(object):
    #TODO: REFAZER AMANHÃ!!
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        changed = set()
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in changed:
                    continue
                if matrix[i][j] == 0:
                    for x in range(ROWS):
                        if matrix[x][j] !=0:
                            matrix[x][j] = 0
                            changed.add((x,j))
                    for x in range(COLS):
                        if matrix[i][x] !=0:
                            matrix[i][x] = 0
                            changed.add((i,x))
    

        
