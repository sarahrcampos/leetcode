import heapq
class Solution(object):
    #Space: O(n)
    #Time: O(k*logn) 
    def getFinalState(self, nums, k, multiplier):
        indexes = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(indexes)
        for _ in range(k):
            m, i = heapq.heappop(indexes) #O(logn)
            nums[i] *= multiplier
            heapq.heappush(indexes, (nums[i], i)) #O(logn)
        return nums

        
