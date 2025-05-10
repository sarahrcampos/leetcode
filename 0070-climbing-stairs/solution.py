class Solution(object):
    #solution using dynamic programming
    #Time: O(n)
    #Space: O(n)
    def climbStairs(self, n):
        cache = {}
        def climb(n2):
            if n2 < 0:
                return 0
            if n2 == 0:
                return 1
            if n2 not in cache:
                cache[n2] = climb(n2-1) + climb(n2-2)
            return cache[n2]
        return climb(n)
                
        
