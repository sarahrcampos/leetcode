class Solution:
    #max(nums[i-1], nums[i] + nums[i-2])
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(1, n):
            calc = nums[i] + (nums[i - 2] if i - 2 >= 0 else 0)
            nums[i] = max(nums[i-1], calc)
        
        return nums[-1]
