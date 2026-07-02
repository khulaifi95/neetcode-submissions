class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, 0
        dp = 0

        for i in range(n - 1, -1, -1):
            dp_i = max(a, nums[i] + b)
            b = a
            a = dp_i
        return dp_i