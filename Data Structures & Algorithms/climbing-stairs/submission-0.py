"""
dp(1) = 1
dp(2) = 2
dp(3) = dp(2) + dp(1)
dp(4) = dp(3) + dp(2)
dp(n) = 1 + dp(n - 1) or 1 + dp(n - 2)
"""

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]