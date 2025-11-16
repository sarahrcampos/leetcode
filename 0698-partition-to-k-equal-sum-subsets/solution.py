class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        
        groups = [0] * k
        length = total // k
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True
            
            for group in range(k):
                if groups[group] + nums[i] <= length:
                    groups[group] += nums[i]
                    if backtrack(i+1):
                        return True
                    groups[group] -= nums[i]
                if groups[group] == 0:
                    break
            
            return False
        
        return backtrack(0)
