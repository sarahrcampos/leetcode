class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                curSum = nums[i]
                continue
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum
                
