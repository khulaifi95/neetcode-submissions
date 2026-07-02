"""
find the longest subarray, containing at most k characters differ with others.
return length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        res = 0
        L = 0

        maxf = 0
        for R in range(len(s)):
            window[s[R]] += 1
            maxf = max(maxf, window[s[R]])
            
            while (R - L + 1) - maxf > k:
                window[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res