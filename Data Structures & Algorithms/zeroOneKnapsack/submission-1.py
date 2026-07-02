class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}

        def dfs(i, capacity):
            if (i, capacity) in memo:
                return memo[(i, capacity)]
            if i == len(profit):
                return 0
            
            res = dfs(i + 1, capacity)
            new_cap = capacity - weight[i]
            if new_cap >= 0:
                with_i = profit[i] + dfs(i + 1, new_cap)
                res = max(with_i, res)
            memo[(i, capacity)] = res
            return res

        return dfs(0, capacity)