#somar tudo
#ir acrescentando na partição, a outra partição vai ter valor total - currSum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if len(nums) == 1 or total%2:
            return False
        
        cache = {}
        def dfs(i, currSum):
            nonlocal total
            if currSum == total//2:
                return True
            if currSum > total//2 or i >= len(nums):
                return False
            if (i, currSum) not in cache:
                cache[(i, currSum)] =  dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)
            return cache[(i, currSum)]

        return dfs(0, 0)

          
