class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        #A[i] = max(A[i-1], A[i-2] + wi)
        def robSubset(subset):
            last, second2last = 0, 0
            for n in subset:
                temp = max(last, second2last + n)
                second2last = last
                last = temp #meu max atual, que vai virar o último do próximo n
            return last
        
        return max(robSubset(nums[1:]), robSubset(nums[:len(nums)-1]))
        

