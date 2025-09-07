#[0] and [-1] cannot be both in the answer
#lets just try force them in the answer and see which one does better
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        withZero = [0] * n
        withZero[0], withZero[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1):
            withZero[i] = max(withZero[i-1], nums[i] + withZero[i - 2])
        
        #force [-1]
        nums[n-2] = max(nums[n-2], nums[n-1])
        for i in range(len(nums)-3, 0, -1):
            nums[i] = max(nums[i+1], nums[i] + nums[i+2])
        
        return max(withZero[-2], nums[1])
        

