class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        memo = [[0]*(COLS+1) for _ in range(ROWS+1)]

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                memo[i][j] = max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1] + (1 if text1[i-1] == text2[j-1] else 0))
        #print(memo)
        return memo[ROWS][COLS]
