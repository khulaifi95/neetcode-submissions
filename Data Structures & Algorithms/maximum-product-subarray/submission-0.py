class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        pref = suf = 0

        for i in range(n):
            pref = nums[i] * (pref or 1)
            suf = nums[n - 1 - i] * (suf or 1)
            res = max(res, max(pref, suf))
        return res