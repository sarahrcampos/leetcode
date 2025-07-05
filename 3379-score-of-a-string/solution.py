class Solution:
    def scoreOfString(self, s: str) -> int:
        count = abs(ord(s[0]) - ord(s[1]))
        for i in range(1, len(s)-1):
            count += abs(ord(s[i]) - ord(s[i+1]))
        return count
