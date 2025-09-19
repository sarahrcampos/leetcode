#intervals = [ [1,3],insert here,[6,9]], newInterval = [2,5]
#[-1,0]
#[4,5]
#[10,12]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:        
        newList = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                return newList + [newInterval] + intervals[i:]
            
            if newInterval[0] <= interval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            else:
                newList.append(interval)
        newList.append(newInterval)
        return newList 
            
#intervals = [[1,3],[6,9]], newInterval = [2,5]
#newInterval = [1, 5]
#
