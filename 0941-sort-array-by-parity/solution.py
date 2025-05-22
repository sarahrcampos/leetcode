class Solution(object):
    #Time: O(n)
    #Space: O(1)
    def sortArrayByParity(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] % 2 and not nums[r]%2:
                nums[l], nums[r] = nums[r], nums[l]
            #if left is even, move l until find an odd number
            if not nums[l] % 2: 
                l += 1
            #if right is odd, move r until find an even number
            if nums[r] % 2:
                r -= 1
        return nums
