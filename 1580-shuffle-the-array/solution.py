class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = 0, len(nums)//2
        res = []
        while y < len(nums):
            res.append(nums[x])
            res.append(nums[y])
            x, y = x+1, y+1
        return res
