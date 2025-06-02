class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}

        def backtrack(i):
            if i in cache:
                return cache[i]
            if i == len(nums)-1:
                cache[i] = True
                return True
            if i >= len(nums) or nums[i] == 0:
                cache[i] = False
                return False           
            
            for j in range(nums[i],0,-1):
                if backtrack(i + j):
                    cache[i] = True
                    return True
            cache[i] = False
            return False
        return backtrack(0)
        
