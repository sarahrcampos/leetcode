class Solution:
    def romanToInt(self, s: str) -> int:
        numeralMapping = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        count = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and numeralMapping[s[i]] < numeralMapping[s[i+1]]:
                count += numeralMapping[s[i+1]] - numeralMapping[s[i]]
                i += 2
            else:
                count += numeralMapping[s[i]]
                i += 1
        return count
