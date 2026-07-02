class Solution:
    def longestPalindrome(self, s: str) -> str:
        x, res = 0, 0
        n = len(s)
        for i in range(n):
            L, R = i, i
            while L >= 0 and R < n and s[L] == s[R]:

                if res < R - L + 1:
                    res = R - L + 1
                    x = L
                L -= 1
                R += 1
            L, R = i, i + 1
            while L >= 0 and R < n and s[L] == s[R]:

                if res < R - L + 1:
                    res = R - L + 1
                    x = L
                L -= 1
                R += 1
        return s[x: x + res]
            