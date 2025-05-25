class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0
        while ps < len(s):
            while pt < len(t) and t[pt] != s[ps]:
                pt += 1
            if pt == len(t):
                return False
            pt, ps = pt + 1, ps + 1
        return True
