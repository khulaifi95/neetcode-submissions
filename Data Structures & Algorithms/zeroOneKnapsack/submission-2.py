class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}

        n = len(profit)

        dp = [[0] * (capacity + 1) for _ in range(n)]

        for c in range(capacity + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        
        for i in range(1, n):
            for c in range(capacity + 1):
                skip = dp[i - 1][c]

                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i - 1][c - weight[i]]
                
                dp[i][c] = max(skip, include)
        
        return dp[n - 1][capacity]

        # def dfs(i, capacity):
        #     if (i, capacity) in memo:
        #         return memo[(i, capacity)]
        #     if i == len(profit):
        #         return 0
            
        #     res = dfs(i + 1, capacity)
        #     new_cap = capacity - weight[i]
        #     if new_cap >= 0:
        #         with_i = profit[i] + dfs(i + 1, new_cap)
        #         res = max(with_i, res)
        #     memo[(i, capacity)] = res
        #     return res

        # return dfs(0, capacity)