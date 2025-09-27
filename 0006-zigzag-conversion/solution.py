class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix, col = [], [""] * numRows
        i, j = 0, 0
        up, cols = False, 1
        while j < len(s):
            col[i] = s[j]
            i += 1 if not up else -1
            j += 1            
            if up or i >= numRows:
                if i >= numRows:
                    i = max(0, numRows-2)
                up = i != 0
                matrix.append(col)
                cols += 1
                col = [""] * numRows
        matrix.append(col) #last col
        res = []
        for j in range(numRows):
            for i in range(cols):
                if matrix[i][j]:
                    res.append(matrix[i][j])

        return "".join(res)
            
