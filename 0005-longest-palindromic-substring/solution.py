class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ""
        for i in range(len(s)):
            # 1 - odd
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if len(s[l+1:r]) > len(longest):
                longest = s[l+1:r]

            #2 - even
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if len(s[l+1:r]) > len(longest):
                longest = s[l+1:r]
        
        return longest
