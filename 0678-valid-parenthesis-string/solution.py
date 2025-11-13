class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        def dfs(i, openParenthesis):
            if i == len(s):
                return openParenthesis == 0
            if (i, openParenthesis) in cache:
                return cache[(i, openParenthesis)]
            if openParenthesis < 0:
                return False
            
            if s[i] == "(":
                cache[(i, openParenthesis)] = dfs(i+1, openParenthesis + 1)
            elif s[i] == ")":
                cache[(i, openParenthesis)] = dfs(i+1, openParenthesis - 1)
            elif s[i] == "*":
                cache[(i, openParenthesis)] = dfs(i+1, openParenthesis) or dfs(i+1, openParenthesis + 1) or dfs(i+1, openParenthesis - 1)
            
            return cache[(i, openParenthesis)]
        return dfs(0, 0)

