class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or currSum > target:
                return            

            #usar i
            curr.append(candidates[i])
            dfs(i+1, curr, currSum + candidates[i])
            curr.pop()

            #não usar i -> nem quaisquer numeros iguais a candidates[i]
            #pular numeros repetidos
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, curr, currSum)
        
        dfs(0, [], 0)
        return res
