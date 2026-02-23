#1 - keep a frequency counter and a heap with size k -> O(nlogk)
#2 - 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        minHeap = []
        for n in nums:
            frequency[n] += 1
        
        for n in frequency:
            heapq.heappush(minHeap, (frequency[n], n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        while minHeap:
            freq, n = heapq.heappop(minHeap)
            res.append(n)
        
        return res

