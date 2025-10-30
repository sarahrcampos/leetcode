class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.lstrip()
        if not s:
            return 0
        if s[0] != "-" and s[0] != "+" and not s[0].isnumeric():
            return 0
            
        
        isNegative = s[0] == "-"
        i = start = 0
        if s[0] == "+" or s[0] == "-":
            i = start = 1
        while i < len(s):
            c = s[i]
            if not c.isnumeric():
                break
            i += 1
            if c == "0":
                continue
        res = s[start:i]
        if not res:
            return 0

        res = int(res) * (-1 if isNegative else 1)
        if res < (-2)**31:
            return (-2)**31
        if res > (2**31 -1):
            return 2**31 - 1
        return res
        
