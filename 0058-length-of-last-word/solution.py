class Solution(object):
    def lengthOfLastWord(self, s):
        st = s.split()
        return len(st[-1])
        
