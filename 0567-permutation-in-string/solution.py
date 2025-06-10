class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters2 = defaultdict(int)
        for c in s1:
            letters2[c] += 1
        
        l, r = 0, 0
        letters1 = defaultdict(int)
        while r < len(s2):
            letters1[s2[r]] += 1
            while letters1[s2[r]] > letters2[s2[r]]:
                letters1[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
            r += 1
        return False

