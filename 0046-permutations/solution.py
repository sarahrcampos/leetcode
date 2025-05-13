class Solution(object):
    def permute(self, nums):
        SIZE_NUMS = len(nums)
        result = []
        used = set()
        def dfs(permutation, size_permutation):
            if size_permutation == SIZE_NUMS:
                result.append(permutation[::])
            for n in nums:
                if n not in used:
                    permutation.append(n)
                    used.add(n)
                    dfs(permutation, size_permutation+1)
                    permutation.pop()
                    used.remove(n)
        dfs([], 0)
        return result
        
