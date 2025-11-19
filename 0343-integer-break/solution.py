class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        for target in range(2, n+1):
            for i in range(1, n):
                if target - i <= 0:
                    break
                dp[target] = max(dp[target],
                            max(i, dp[i]) * max(target-i, dp[target-i]))
        
        return dp[n]
