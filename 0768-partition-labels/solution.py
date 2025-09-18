class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rangeSeen = {}
        for i in range(len(s)):
            c = s[i]
            if c not in rangeSeen:
                rangeSeen[c] = [i, i]
            else:
                rangeSeen[c][1] = i #0 = firstSeen, 1 = lastSeen
        curBegin = curEnd = 0
        ranges = [0]
        for c in s:
            firstSeen, lastSeen = rangeSeen[c]
            #print(ranges)
            if firstSeen > curEnd:                
                curBegin, curEnd = firstSeen, lastSeen
                ranges.append(curEnd - curBegin + 1)
                continue
            curEnd = max(lastSeen, curEnd)
            ranges[-1] = curEnd - curBegin + 1
            #print(curBegin, curEnd)
        return ranges
