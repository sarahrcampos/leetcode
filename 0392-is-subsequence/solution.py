from collections import deque
class Solution(object):
    def isSubsequence(self, s, t):
        q = deque(s)
        for c in t:
            if q and q[0] == c:
                q.popleft()
        return len(q) == 0
        
