class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, currSum):
            if currSum > target or i >= len(candidates):
                return
            if currSum == target:
                res.append(curr.copy())
                return
            
            #não usar i
            dfs(i+1, curr, currSum)

            #usar i
            curr.append(candidates[i])

            #usar i de novo
            dfs(i, curr, currSum + candidates[i])

            curr.pop()

        dfs(0, [], 0)
        return res
