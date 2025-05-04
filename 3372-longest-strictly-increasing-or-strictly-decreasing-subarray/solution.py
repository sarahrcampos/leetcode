class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc, dec, result = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dec, inc = 1, 1
            elif nums[i] < nums[i-1]:
                dec, inc = dec + 1, 1                
            else:
                inc, dec = inc + 1, 1
            result = max(inc, dec, result)
        return result
        
