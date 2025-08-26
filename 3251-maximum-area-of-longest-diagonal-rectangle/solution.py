class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal, maxArea = 0, 0

        for length, width in dimensions:
            diagonal = math.sqrt(length ** 2 + width ** 2)
            area = length * width
            if diagonal > maxDiagonal or (diagonal == maxDiagonal and area > maxArea):
                maxDiagonal = diagonal
                maxArea = area
        
        return maxArea
            
