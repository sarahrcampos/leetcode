class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i-1]: #skip duplicates to avoid duplicated triplets
                continue
            l, r = i+1, len(nums)-1
            while l < r:                
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 #escolher arbitrariamente mover o l, pq se for a decisão errada vai se ajeitar na próxima iteração
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1      
        return res
