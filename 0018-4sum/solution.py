class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            while j < len(nums):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    currSum = nums[i] + nums[j] + nums[l] + nums[r]
                    if currSum > target:
                        r -= 1
                    elif currSum < target:
                        l += 1
                    else:
                        print(i,j,l,r)
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l += 1
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
        return res
