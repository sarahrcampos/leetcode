class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = sum(range(0,len(nums)+1))
        calculated = sum(nums)
        return expected - calculated
