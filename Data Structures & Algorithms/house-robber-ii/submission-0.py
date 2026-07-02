class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def robb(num):
            k = len(num)
            a, b, i = 0, 0, 0
            for i in range(k - 1, -1, -1):
                i = max(a, b + num[i])
                b = a
                a = i
            return i
        return max(
            robb(nums[1:]),
            robb(nums[:-1])
        )