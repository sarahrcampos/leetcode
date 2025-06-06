class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            current = (right - left) * min(height[left], height[right])
            area = max(area, current)
            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                if min(height[left], height[right-1]) > min(height[left+1], height[right]):
                    right -= 1
                else:
                    left += 1
        return area
        
