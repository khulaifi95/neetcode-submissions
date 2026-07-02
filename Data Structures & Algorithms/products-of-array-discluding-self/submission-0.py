class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prefix_prod = [1 for _ in range(n)]
        right_prefix_prod = [1 for _ in range(n)]
        for i in range(1, n):
            left_prefix_prod[i] = left_prefix_prod[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right_prefix_prod[i] = right_prefix_prod[i + 1] * nums[i + 1]
        res = [0] * n
        for i in range(n):
            res[i] = left_prefix_prod[i] * right_prefix_prod[i]
        return res
        
        