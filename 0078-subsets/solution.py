class Solution(object):
    #Time: O(2^n)
    def subsets(self, nums):
        result = []
        def dfs(i, subset):
            if i == len(nums):
                result.append(subset)
                return
            dfs(i+1, subset) #don't choose the number
            dfs(i+1, subset + [nums[i]]) #choose the number
        dfs(0, [])
        return result
        
