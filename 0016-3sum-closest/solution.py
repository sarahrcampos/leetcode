class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = float("inf")
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j + 1, len(nums)-1
                while l <= r:
                    m = (l+r)//2
                    currSum = nums[i] + nums[j] + nums[m]
                    if abs(target - currSum) < abs(target - closestSum):
                        closestSum = currSum
                    if currSum > target:
                        r = m - 1
                    elif currSum < target:
                        l = m + 1
                    else:
                        return currSum
        return closestSum
                    
