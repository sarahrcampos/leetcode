class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for num in nums:
            count |= 1 << num
        for i in range(n+1):
            iFlag = count & 1
            if not iFlag:
                return i
            count = count >> 1
        
