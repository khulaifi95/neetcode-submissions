class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        def dfs(i, remain):
            if i >= len(coins):
                return 0
            
            if remain == 0:
                return 1
            
            if memo[i][remain] != -1:
                return memo[i][remain]
            
            if coins[i] > remain:
                res = 0
            else:
                res = dfs(i + 1, remain) + dfs(i, remain - coins[i])
            
            memo[i][remain] = res
            return res

        return dfs(0, amount)