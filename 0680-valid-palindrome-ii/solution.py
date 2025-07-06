class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validate(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return validate(l+1, r) or validate(l, r-1)
            l, r = l+1, r-1
        return True

        
