class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        maximum = 0
        while r < len(nums):
            if nums[r] == 0:
                if nums[l] == 1:
                    maximum = max(maximum, r - l)
                l = r + 1
            r += 1
        maximum = max(maximum, r - l)        
        return maximum
            
