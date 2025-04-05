class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        small = 0
        minimum = float("inf")
        for big in range(k-1, len(nums)):
            diff = nums[big] - nums[small]
            minimum = min(minimum, diff)
            small += 1
        return minimum


        
