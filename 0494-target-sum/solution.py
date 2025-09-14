class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, total):
            if i == len(nums) and total == target:
                return 1
            if i >= len(nums):
                return 0

            if (i, total) not in cache:
                cache[(i, total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            return cache[(i, total)]
        
        return dfs(0, 0)
