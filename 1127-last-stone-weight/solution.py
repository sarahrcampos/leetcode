import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y-x)
        return 0 if len(heap) == 0 else -heap[0]

        
