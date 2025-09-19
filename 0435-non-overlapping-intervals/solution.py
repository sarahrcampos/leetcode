class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr[1]:
                count +=1
                if curr[1] < intervals[i][1]: #manter o atual
                    continue
            curr = intervals[i]
        return count
