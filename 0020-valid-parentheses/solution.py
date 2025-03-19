class Solution(object):
    def isValid(self, s):
        mapOpen = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []

        for c in s:
            if c in mapOpen:
                stack.append(c)
            else:
                if(len(stack) <= 0): 
                    return False
                last = stack.pop()
                if(mapOpen[last] != c):
                    return False
        return len(stack) == 0
        
