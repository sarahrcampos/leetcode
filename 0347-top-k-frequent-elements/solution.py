class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort -> O(n)
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
