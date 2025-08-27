class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #nlogn
        def twoSum(start, end, target):
            res = []
            l, r = start, end
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([-target, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return res

        answer = []
        i = 0
        while i < len(nums):
            answer += twoSum(i+1, len(nums)-1, -nums[i])
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1        
        return answer


#[-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
