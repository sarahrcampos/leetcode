class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < 0:
                return i
            nums[i] = -nums[i]
            i = -nums[i]
