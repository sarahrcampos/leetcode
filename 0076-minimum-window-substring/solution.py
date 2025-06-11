class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapT = defaultdict(int)
        for c in t:
            mapT[c] += 1
        
        l = 0
        mapS = defaultdict(int)
        minSubstring = s
        curSubstring, curT = "", ""
        for r in range(len(s)):
            mapS[s[r]] += 1
            curSubstring += s[r]
            if mapS[s[r]] <= mapT[s[r]]:
                curT += s[r]

            while l < len(s) and mapS[s[l]] > mapT[s[l]]:
                curSubstring = curSubstring[1:]
                mapS[s[l]] -= 1
                l += 1

            if len(curT) >= len(t) and len(curSubstring) < len(minSubstring):
                    minSubstring = curSubstring
        return minSubstring if len(curT) == len(t) else ""
