class Solution(object):
    #Time: O(n)
    #Space: O(1)
    def moveZeroes(self, nums):
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        
