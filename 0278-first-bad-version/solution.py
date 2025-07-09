# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

#all the versions after a bad version are also bad
    #if true -> candidate to be the first -> move search range to the left
    #else -> move search range to the right

#n = 5, bad = 4
# 1,2,3,4,5
# f,f,f,t,t
class Solution:
    def firstBadVersion(self, n: int) -> int:
        candidate = n
        left, right = 1, n
        while left <= right:
            middle = (left+right)//2
            if isBadVersion(middle):
                candidate = middle
                right = middle - 1
            else:
                left = middle + 1
        return candidate


#n=3, bad = 1
#1,2,3
#t,t,t
#
