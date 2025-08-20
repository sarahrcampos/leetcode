class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        for c in t:
            countT[c] += 1
        
        left,right = 0,0
        countWindow = defaultdict(int)
        minLength = float("inf")
        minL, minR = 0, 0        
        window = set()

        while right < len(s):
            if s[right] in countT:
                countWindow[s[right]] += 1
                if countWindow[s[right]] == countT[s[right]]:
                    window.add(s[right])

            while left < right and (s[left] not in countT or countWindow[s[left]] > countT[s[left]]):
                if s[left] in countT:
                    countWindow[s[left]] -= 1
                left += 1
            
            if len(window) == len(countT): #ja tenho tds os caracteres necessarios
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minL = left
                    minR = right
            right = right + 1
            

        return "" if minLength == float("inf") else s[minL:minR+1]

#                   L     R
#"TTTADOBBEACODEBANCBACTTTT", t = "ABC"
#countT = { A: 1, B: 1, C: 1}
#window = A,B,C
#minLength = 4, minL = 7, minR = 10
