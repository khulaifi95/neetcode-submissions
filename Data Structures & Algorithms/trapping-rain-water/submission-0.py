class Solution:
    def trap(self, height: List[int]) -> int:
        # when will the rain be trapped?
        # at given position i, you have height[l] > height[i] and height[r] > height[i]
        n = len(height)
        maxl, maxr = 0, 0
        res = 0
        lb = [0 for _ in range(n)]
        rb = [0 for _ in range(n)]
        for i in range(n):
            maxl = max(maxl, height[i])
            lb[i] = maxl
        for j in range(n - 1, -1, -1):
            maxr = max(maxr, height[j])
            rb[j] = maxr
        
        for i in range(n):
            curr = min(lb[i], rb[i]) - height[i]
            res += curr
        return res