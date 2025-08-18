class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freqMap = defaultdict(int)
        for c in s:
            freqMap[c] += 1
        for c in t:
            if c not in freqMap or freqMap[c] == 0:
                return False
            freqMap[c] -= 1
        
        return True
