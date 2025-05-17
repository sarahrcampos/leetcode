class Solution(object):
    def searchInsert(self, nums, target):
        SIZE = len(nums)
        left, right = 0, SIZE - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return right + 1
        
