class Solution(object):
    def combine(self, n, k):
        result = []
        def dfs(i, j, combination):            
            if j == k:
                result.append(combination[::])
                return
            if i > n:
                return
            #do not add i
            dfs(i+1, j, combination)
            
            #add i
            combination.append(i)
            dfs(i+1, j+1, combination)
            combination.pop()
        dfs(1,0,[])
        return result
        
