class Solution(object):
    def makeGood(self, s):
        stack = []
        for c in s:
            if not stack or abs(ord(stack[-1]) - ord(c)) != 32:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)
        
