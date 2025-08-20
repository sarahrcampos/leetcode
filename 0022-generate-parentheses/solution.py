class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def generate(opened, closed, curr):
            if len(curr) == n*2:
                res.append(curr)
                return
            
            if opened < n:
                generate(opened+1, closed, curr + "(")

            if opened > 0 and closed < opened:
                generate(opened, closed + 1, curr + ")")
                
        
        generate(0,0,"")
        return res
