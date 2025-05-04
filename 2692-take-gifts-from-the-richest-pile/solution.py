import heapq
class Solution(object):
    def pickGifts(self, gifts, k):
        heap, total = [], 0
        for gift in gifts:
            heap.append(-gift)
            total += gift
        heapq.heapify(heap)
        for i in range(k):
            maximum = -heapq.heappop(heap)
            new = int(math.sqrt(maximum))
            total -= (maximum - new)
            heapq.heappush(heap, -new)
        return total
        
        
