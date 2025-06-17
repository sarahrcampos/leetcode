class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(i, open, close, current):
            if i == n*2:
                res.append(current)
                return
            if open < n:
                generate(i+1, open + 1, close, current + '(')
            if close < open:
                generate(i+1, open, close + 1, current + ')')
        
        generate(1, 1, 0, '(')
        return res
