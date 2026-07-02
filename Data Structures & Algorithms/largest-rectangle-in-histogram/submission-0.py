"""
heights vec[int] -> height of a bar
width bar: 1

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            cur = heights[i]

            R = i + 1
            while R < n and heights[R] >= cur:
                R += 1
            
            L = i
            while L >= 0 and heights[L] >= cur:
                L -= 1
            
            R -= 1
            L += 1
            res = max(res, cur * (R - L + 1))
        
        return res