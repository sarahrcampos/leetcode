#[[-1,0], [1,3],[2,6],[8,10],[11,14], [15,18]]
#[14,17] [8,10]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newList = []
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                newList.append(newInterval)
                newInterval = interval
                continue
            if newInterval[0] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])                
                newInterval[1] = max(interval[1], newInterval[1])
            else:
                newList.append(interval)
        newList.append(newInterval)
        return newList
