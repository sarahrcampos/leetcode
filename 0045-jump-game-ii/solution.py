class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = [len(nums)] * len(nums)
        minJumps[-1] = 0
        nextTrue = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= nextTrue:
                for j in range(nums[i] + 1): 
                    if i+j >= len(nums):
                        break
                    minJumps[i] = min(minJumps[i], minJumps[i + j] + 1)                    
                nextTrue = i
        return minJumps[0]
