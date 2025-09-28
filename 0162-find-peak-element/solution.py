#     lm  r
# [1,2,3,1,6]
# [1, 2]  [3, 1 6]
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def findPeakElementInRange(startIndex, endIndex):
            if startIndex > endIndex:
                return -1
            
            middleIndex = (startIndex + endIndex) // 2
            leftNeighbor = nums[middleIndex - 1] if (middleIndex - 1) >= 0 else float("-inf")
            rightNeighbor = nums[middleIndex + 1] if (middleIndex + 1) < len(nums) else float("-inf")
            if leftNeighbor < nums[middleIndex] and rightNeighbor < nums[middleIndex]:
                return middleIndex
            
            return max(findPeakElementInRange(startIndex, middleIndex - (1 if leftNeighbor > nums[middleIndex] else 2)), 
                    findPeakElementInRange(middleIndex + (1 if rightNeighbor > nums[middleIndex] else 2), endIndex))
        
        return findPeakElementInRange(0, len(nums) - 1)

