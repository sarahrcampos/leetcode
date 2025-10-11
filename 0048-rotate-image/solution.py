class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        start, end = 0, len(matrix) - 1
        while start < end:
            for offset in range(0, end-start):                
                #top-left
                topleft = matrix[start][start + offset]                

                #bottom-left = matrix[end-offset][start]
                #top-left -> bottom-left
                matrix[start][start + offset] = matrix[end-offset][start]

                #bottomright = matrix[end][end-offset]
                #bottom-left -> bottom-right
                matrix[end-offset][start] = matrix[end][end-offset]
                
                #bottom-right = matrix[start + offset][end]
                #bottom-right -> top-right
                matrix[end][end-offset] = matrix[start + offset][end]

                #top-right -> topleft
                matrix[start + offset][end] = topleft
                
                
            start, end = start + 1, end - 1
        
