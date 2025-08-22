class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r+l) // 2
            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                return nums[l]
            if m - 1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]
            
            if nums[m] < nums[r]:
                r -= 1
            else:
                l += 1
        
        return nums[l]
