class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        maximum, current = 0, 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in visited:
                current +=1
                visited.add(s[r])
            else:
                while s[l] != s[r]:
                    visited.remove(s[l])
                    current -= 1
                    l = l + 1
                l = l + 1
            r += 1
            maximum = max(maximum, current)
        return maximum
        
