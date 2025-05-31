class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res= []
        inserted = False
        for lowerBound, upperBound in intervals:
            if upperBound < newInterval[0]:
                res.append([lowerBound, upperBound])
            elif newInterval[1] < lowerBound:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append([lowerBound, upperBound])
            else:
                newInterval = [min(lowerBound, newInterval[0]), max(upperBound, newInterval[1])]
        if not inserted:
            res.append(newInterval)

        return res
