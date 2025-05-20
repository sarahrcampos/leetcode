class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        l, r = 0, 1
        SIZE = len(colors)
        count, res = 1, 0
        while l < SIZE:
            i = r % SIZE
            count += 1
            if colors[i] == colors[i-1]:
                l = min(SIZE, r)
                count = 1
            elif count == k:
                res += 1
                l += 1
                count -= 1
            r += 1
        return res
        
