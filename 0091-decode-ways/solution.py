class Solution:
    def numDecodings(self, s: str) -> int:
        #bottom-up
        first, second = 1 if s[-1] != '0' else 0, 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                second, first = first, 0
                continue
            temp = first
            first = first + (second if s[i] == '1' or (s[i] == '2'and i+1 < len(s) and int(s[i+1]) <= 6) else 0)
            second = temp
        return first


        

        #top-down
        # cache = {}
        # def count(i):
        #     if i < len(s) and s[i] == '0':
        #         return 0
        #     if i >= len(s) - 1:
        #         cache[i] = 1
        #     if i in cache:
        #         return cache[i]            
        #     solo = count(i+1)
        #     double = count(i+2) if (i + 1 < len(s) and 
        #                                 (s[i] == '1' or 
        #                                 (s[i] == '2' and int(s[i+1]) <= 6))
        #                             ) else 0
        #     cache[i] = solo + double
        #     return cache[i]
        
        # return count(0)
