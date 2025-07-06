class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd, minEven = 0, len(s)
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1            
        for count in counter.values():
            if count % 2:
                maxOdd = max(maxOdd, count)
            else:
                minEven = min(minEven, count)
        return maxOdd - minEven
        
