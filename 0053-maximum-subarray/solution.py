class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            total = nums[i] if total < 0 else (total + nums[i])
            maximum = max(maximum, total)
        return maximum

