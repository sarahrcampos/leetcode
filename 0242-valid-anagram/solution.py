class Solution(object):
    #Time: O(n+m)
    #Space: O(n)
    def isAnagram(self, s, t):
        map = {}
        for c in s:
            map[c] = 1 + map.get(c, 0)
        for c in t:
            if c not in map:
                return False
            map[c] -= 1
            if map[c] == 0:
                del map[c]
        return len(map) == 0
        
        
        
