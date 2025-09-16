#BOTTOM-UP:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)
        cache = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for i in range(ROWS):
            cache[i][COLS] = ROWS - i
        for j in range(COLS):
            cache[ROWS][j] = COLS - j
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i][j+1],
                        cache[i+1][j],
                        cache[i+1][j+1]
                    )
        #print(cache)
        return cache[0][0]

#TOP-DOWN
# cache = {}
#         def dfs(i, j):
#             if i < len(word1) and j == len(word2):
#                 return len(word1) - i
#             if i == len(word1) and j < len(word2):
#                 return len(word2) - j
#             if i == len(word1) and j == len(word2):
#                 return 0
            
#             if (i,j) in cache:
#                 return cache[(i,j)]
            
#             if word1[i] == word2[j]:
#                 cache[(i,j)] = dfs(i + 1, j + 1)
#             else:
#                 insert = 1 + dfs(i, j + 1)
#                 delete = 1 + dfs(i+1, j)            
#                 replace = 1 + dfs(i+1, j+1)
#                 cache[(i,j)] = min(insert, delete, replace)
#             return cache[(i,j)]
#         return dfs(0,0)

