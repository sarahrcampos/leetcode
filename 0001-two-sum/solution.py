class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {n:i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            if target - n in indices and indices[target - n] != i:
                return [i, indices[target - n]]
