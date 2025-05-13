class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        memo = {}
        def dfs(soma, combination, frequency):
            if soma == target:
                result.append(combination)
                return
            if soma > target:
                return
            for i in range(len(candidates)):
                if candidates[i] <= target:
                    frequency[i] += 1
                    if tuple(frequency) not in memo:
                        dfs(soma+candidates[i], combination + [candidates[i]], frequency)
                        memo[tuple(frequency)] = True
                    frequency[i] -= 1
        
        dfs(0,[], [0]*len(candidates))
        return result
        
