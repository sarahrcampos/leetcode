class Solution:
    #Time: O(nlogk)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        minHeap = []
        for num, count in map.items():
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for count, num in minHeap:
            res.append(num)
        return res
