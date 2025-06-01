class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        current = intervals[0]
        
        for i in range(1, len(intervals)):
            if current[1] < intervals[i][0]: #current upperbound is less than intervals[i] lowerbound, so current is not in this interval
                res.append(current[::])
                current = intervals[i]
            elif intervals[i][1] < current[0]:
                res.append(intervals[i][::])
            else:
                current[0] = min(current[0], intervals[i][0])
                current[1] = max(current[1], intervals[i][1])
        res.append(current)
        return res
