class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest, smallest = 1, 1
        maximum = nums[0]
        for curr in nums:            
            calcMin = curr * smallest
            calcMax = curr * largest

            smallest = min(calcMin, calcMax, curr)
            largest = max(calcMin, calcMax, curr)
            maximum = max(maximum, largest)

        return maximum

