class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        left, right = 0, len(nums)-1
        while (left <= right):
            if nums[left] != val:
                left += 1
            if nums[right] == val:
                right -= 1
                count += 1
            
            if left > right:
                break

            if nums[left] == val and nums[right] != val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
            

        return len(nums) - count
        
