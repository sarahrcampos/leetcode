class Solution(object):
    def majorityElement(self, nums):
        map = {}
        for element in nums:
            map[element] = 1 if element not in map else map[element] + 1
        for key, value in map.items():
            if value > len(nums)//2:
                return key
        return -1
        
