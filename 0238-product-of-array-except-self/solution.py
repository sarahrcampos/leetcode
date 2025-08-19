class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * (len(nums) + 1)

        for i in range(1, len(nums)):
            answer[i] = nums[i-1] * answer[i-1]
        
        for i in range(len(nums)-2, -1,-1):
            nums[i] *= nums[i+1]
        
        answer[-1] = answer[-2]
        print(answer)
        for i in range(len(answer)-2, 0, -1):
            answer[i] = answer[i-1] * nums[i]
        
        return answer[1:]
        
# [-1,1,0,-3,3]
#prefix[i] = answer[i]
# [1,-1,-1,0,0,1]

#suffix[i] = nums[i+1]
# [0,0,0,-9,3]

#[1,0,0,9,0,0]
