class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        cache = [False] * len(s)
        for i in range(len(s)-1, -1,-1):
            for j in range(len(s), i, -1):
                if s[i:j] in wordDict and (j == len(s) or cache[j]):
                    cache[i] = True
                    break        
        return cache[0]
