class Solution(object):
    def isValid(self, s):
        pairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for parentheses in s:
            if parentheses in pairs:
                stack.append(parentheses)
                continue
            if not stack:
                return False
            opened = stack.pop()
            if pairs[opened] != parentheses:
                return False
        return not stack
