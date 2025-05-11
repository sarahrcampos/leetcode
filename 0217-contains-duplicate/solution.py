class Solution(object):
    #Time: O(n)
    #Space: O(n)
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
        
