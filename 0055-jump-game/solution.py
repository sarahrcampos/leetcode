class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nextTrue = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= nextTrue: #can reach
                nextTrue = i
        return nextTrue == 0
