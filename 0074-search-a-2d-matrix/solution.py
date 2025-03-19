class Solution(object):
    def searchMatrix(self, matrix, target):
        #analisar a linha
        ROWS, COLS = len(matrix), len(matrix[0])
        s, e = 0, ROWS - 1
        while s <= e:
            i = (s + e)//2
            if target > matrix[i][-1]:
                s = i + 1
            elif target < matrix[i][0]:
                e = i - 1
            else:
                break
        if s > e:
            return False
        i = (s + e)//2
        s, e = 0, COLS - 1        
        #to na linha certa, agr vou ver as colunas... abraços
        while(s <= e):
            j = (s + e)//2
            if(target == matrix[i][j]):
                return True
            elif(target > matrix[i][j]):
                s = j + 1
            else:
                e = j - 1
        return False
        
