class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i in range(len(heights)):
            newI = i
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                largest = max(largest, (i-index) * height)
                newI = index
            stack.append([newI, heights[i]])

        #for the rectangles that weren't stopped from expanding
        while stack:
            index, height = stack.pop()
            largest = max(largest, (len(heights)-index) * height)

        return largest
    
#[2,1,2] 

        
