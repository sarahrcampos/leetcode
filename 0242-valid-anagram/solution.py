class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = defaultdict(int)
        for c in s:
            frequency[c] += 1
        for c in t:
            frequency[c] -= 1
            if frequency[c] < 0:
                return False
            if frequency[c] == 0:
                del frequency[c]
        
        return len(frequency) == 0
