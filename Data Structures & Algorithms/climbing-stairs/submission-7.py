"""
dp(1) = 1
dp(2) = 2
dp(3) = dp(2) + dp(1)
dp(4) = dp(3) + dp(2)
dp(n) = 1 + dp(n - 1) or 1 + dp(n - 2)
"""

class Solution:

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one