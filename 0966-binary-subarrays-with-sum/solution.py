class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSums = {0:1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            diff = currSum - goal
            count += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        
        return count
