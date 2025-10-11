class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = right = 0
        windowSize = len(needle)
        currNeedle = 0

        while right < len(haystack):

            if haystack[right] != needle[currNeedle]:
                currNeedle = 0
                left += 1
                while left < right and haystack[left] != needle[0]:
                    left += 1
                right = left
                continue
            
            if (right - left + 1) == windowSize:
                return left

            currNeedle += 1
            right += 1
        return -1

#windowSize = 5

#           l   r
#haystack = leetcode

#           c    
#needle   = leeto

