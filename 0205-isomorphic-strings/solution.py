class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapFrom = {}
        mapTo = {}
        for i in range (0, len(s)):
            if s[i] in mapFrom and t[i] != mapFrom[s[i]]:
                return False
            if s[i] not in mapFrom:
                if t[i] in mapTo:
                    return False
                mapFrom[s[i]] = t[i]
                mapTo[t[i]] = s[i]
        return True
                
        
