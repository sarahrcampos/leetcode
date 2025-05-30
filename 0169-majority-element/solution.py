class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        total = 1
        for i in range(1,len(nums)):
            if nums[i] != current:
                total -= 1
            else:
                total += 1
            if not total:
                current = nums[i]
                total = 1
        return current
