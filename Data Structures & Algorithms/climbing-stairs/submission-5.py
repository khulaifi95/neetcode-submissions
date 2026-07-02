"""
dp(1) = 1
dp(2) = 2
dp(3) = dp(2) + dp(1)
dp(4) = dp(3) + dp(2)
dp(n) = 1 + dp(n - 1) or 1 + dp(n - 2)
"""

class Solution:

    def climbStairs(self, n: int) -> int:
        mem = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if mem[i] != -1:
                return mem[i]
            mem[i] = dfs(i + 1) + dfs(i + 2)
            return mem[i]
        return dfs(0)