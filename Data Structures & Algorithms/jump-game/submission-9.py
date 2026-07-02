class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n - 1:
                return True
            if nums[i] == 0:
                return False
            end = min(n - 1, i + nums[i])

            for j in range(end, i, -1):
                if dfs(j):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return False
        return dfs(0)