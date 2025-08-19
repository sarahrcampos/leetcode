class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = { n: i for i, n in enumerate(nums) }
        cache = {}
        lcs = 0
        
        def sequence(n):
            if n not in map:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = 1 + sequence(n+1)
            return cache[n]
        
        for n in nums:
            if n in cache:
                continue
            lcs = max(lcs, sequence(n))
        
        return lcs
            
#100,4,200,1,3,2,5,6
#sequence = 1
#cache[100] = 1
#lcs = 1
#cache[4] = 3


