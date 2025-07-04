class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [0] * (m +1)
        for i in range(n):
            current = [0]*(m+1)
            for j in range(m):
                if text1[j] == text2[i]:
                    current[j+1] = memo[j] + 1
                else:
                    current[j+1] = max(current[j], memo[j+1])
            memo = current
        return memo[-1]
