class Solution:
    def intToRoman(self, num: int) -> str:
        power = 0
        res = []
        symbols = {0: ["I", "V"], 1: ["X", "L"], 2: ["C", "D"], 3: ["M"]}
        while num:
            digit = num%10
            num = num//10
            if digit == 9:
                res.append(symbols[power][0] + symbols[power + 1][0])
                power += 1
                continue
            if digit == 4:
                res.append(symbols[power][0] + symbols[power][1])
                power+=1
                continue
            if digit < 4:
                for _ in range(digit):
                    res.append(symbols[power][0])
            else:
                for _ in range(digit - 5):
                    res.append(symbols[power][0])
                res.append(symbols[power][1])
            power+=1
        return "".join(res[::-1])
