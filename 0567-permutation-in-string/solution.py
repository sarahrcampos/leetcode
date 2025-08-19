class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        l = 0
        countS, countWindow = defaultdict(int), defaultdict(int)
        for c in s1:
            countS[c] += 1

        for r in range(len(s2)):
            countWindow[s2[r]] += 1
            if r - l + 1 == windowSize:
                # print(countWindow)
                # print(countS)
                if countWindow == countS:
                    return True
                countWindow[s2[l]] -= 1
                if not countWindow[s2[l]]:
                    del countWindow[s2[l]]
                l += 1


        return False
