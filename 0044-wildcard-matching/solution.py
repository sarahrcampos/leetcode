class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def backtrack(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            elif j == len(p) - 1 and p[j] == "*":
                return True
            elif i >= len(s) and p[j] == "*":
                while j < len(p) and p[j] == "*":
                    j += 1
                return i >= len(s) and j >= len(p)
            elif i >= len(s) or j >= len(p):
                return False

            if p[j] == "*":
                a = i
                while j < len(p)-1 and p[j] == "*":
                    j += 1
                while a < len(s):                    
                    cache[(a,j)] = backtrack(a, j)
                    if cache[(a,j)]:
                        cache[(i,j)] = True
                        return True
                    a += 1
            elif p[j] == "?":
                cache[(i, j)] = backtrack(i+1, j+1)
                return cache[(i,j)]		
            elif i < len(s) and s[i] == p[j]:
                cache[(i,j)] = backtrack(i+1, j+1)
                return cache[(i,j)]
            
            cache[(i,j)] = False
            return False

        return backtrack(0,0)
