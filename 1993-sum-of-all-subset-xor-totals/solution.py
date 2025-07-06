class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, curXor):
            if index >= len(nums):
                return curXor
            
            return dfs(index+1, curXor) + dfs(index+1, curXor ^ nums[index])
        
        return dfs(0, 0)

