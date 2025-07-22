#array of integers nums containing n + 1 integers
# each integer is in the range [1, n] inclusive
#There is only one repeated number in nums, return this repeated number.
#without extra space and without modyfing the array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #the array goes from 0 to n+1
        #we use the indices as the elements
        #if we already visited that index, that is the one repetead.
        index = 0
        while nums[index] > 0:
            nums[index] = (-1) * nums[index]
            index = (-1) * nums[index]
        return index
            
    
    # 0,   1,  2,  3, 4 -> index
    # -1, -3, -4, -2, -2
