class Solution(object):
    #Space: O(2n)
    #Time: O(klogn)
    def kClosest(self, points, k):
        heap = [ [x**2 + y**2, x, y] for x, y in points]
        heapq.heapify(heap)
        return [ heapq.heappop(heap)[1:3] for _ in range(k) ]
        
