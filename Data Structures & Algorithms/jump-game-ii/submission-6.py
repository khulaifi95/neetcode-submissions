class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        sys.setrecursionlimit(2000)
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n - 1:
                return 0
            end = min(n - 1, i + nums[i])
            min_val = float("inf")
            for j in range(end, i, -1):
                min_val = min(min_val, 1 + dfs(j))
            memo[i] = min_val
            return memo[i]

        return dfs(0)