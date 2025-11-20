class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minNum = deque()
        maxNum = deque()
        maxLength = 1
        l = 0
        for r in range(len(nums)):
            # print(l, r)
            # print(minNum)
            # print(maxNum)
            while (minNum and abs(nums[r] - minNum[0]) > limit) or (maxNum and abs(nums[r] - maxNum[0]) > limit):
                if minNum and nums[l] == minNum[0]:
                    minNum.popleft()
                if maxNum and nums[l] == maxNum[0]:
                    maxNum.popleft()
                l += 1
            
            while minNum and nums[r] < minNum[-1]:
                minNum.pop()            
            minNum.append(nums[r])

            while maxNum and nums[r] > maxNum[-1]:
                maxNum.pop()            
            maxNum.append(nums[r])

            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
            
