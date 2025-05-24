class Solution(object):
    def letterCombinations(self, digits):
        letters = {
            "2": [97,99],
            "3": [100,102],
            "4": [103,105],
            "5": [106,108],
            "6": [109,111],
            "7": [112,115],
            "8": [116,118],
            "9": [119,122]
        }
        res = []

        def backtrack(i, current):
            if len(current) == len(digits):
                res.append("".join(current))
                return
            if i == len(digits):
                return
            for letter in range(letters[digits[i]][0], letters[digits[i]][1]+1):
                current.append(str(unichr(letter)))
                backtrack(i+1,current)
                current.pop()

        if digits:
            backtrack(0,[])


        return res
        
