class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, suffix = 0, sum(nums)
        print(suffix)
        for i in range(len(nums)):
            suffix -= nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]
            
        return -1

#[1, 7, 3,6, 5, 6]
#[0, 1, 8,11,17,22]
#[27,20,17,11,6,0]
