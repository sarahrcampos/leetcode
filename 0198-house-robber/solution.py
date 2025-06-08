class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        if len(nums) == 1:
            return nums[0]

        def dfs(i, current):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0

            notSteal = dfs(i+1, current)
            steal = dfs(i+2, current) + nums[i]
            cache[i] = max(notSteal, steal)
            return cache[i]
        dfs(0, 0)
        return max(cache[0], cache[1])
            
