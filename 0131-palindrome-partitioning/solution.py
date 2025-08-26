class Solution:
    #aab
    #0, []
    #i = 0
    #1, [a]
    #i = 1
    #2, [a,a]
    #i = 2
    #3, [a,a,b]
    #res = [[a,a,b]]
    #1, [a]
    #i = 2
    #0, []
    #i = 1
    #3, [aa]

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, curr):
            if start >= len(s):
                res.append(curr.copy())
                return
            
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    curr.append(s[start:i+1])
                    backtrack(i+1, curr)
                    curr.pop()

        backtrack(0,[])
        return res
    
    def isPalindrome(self, s:str, l:int, r:int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
