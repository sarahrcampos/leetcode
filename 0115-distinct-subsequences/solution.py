#BOTTOM-UP:
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s), len(t)
        dp = [0] * (COLS + 1)
        dp[-1] = 1
        for i in range(ROWS-1, -1, -1):
            newDP = [0] * (COLS + 1)
            newDP[-1] = 1
            for j in range(COLS-1, -1, -1):
                if s[i] != t[j]:
                    newDP[j] = dp[j] #pular
                else:
                    newDP[j] = dp[j] + dp[j+1] #pular e usar
            dp = newDP
        return dp[0]

#TOP-DOWN:
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         cache = {}
#         def dfs(i, j):
#             if j == len(t):
#                 return 1
#             if i >= len(s):
#                 return 0
#             if s[i] != t[j] and (i, j) not in cache:
#                 cache[(i,j)] = dfs(i+1, j) #pular
#             elif (i, j) not in cache:
#                 cache[(i,j)] = dfs(i+1, j) + dfs(i+1, j+1)
#             return cache[(i,j)]
                
#         return dfs(0,0)
