class Solution(object):
    #O(nlogn)
    def findContentChildren(self, g, s):
        count = 0
        g.sort() #O(nlogn)
        s.sort() #O(nlogn)
        greed, size = 0, 0
        while size < len(s) and greed < len(g): #O(n)
            if(s[size] >= g[greed]):
                count += 1
                greed += 1       
            size += 1     
        return count
        
