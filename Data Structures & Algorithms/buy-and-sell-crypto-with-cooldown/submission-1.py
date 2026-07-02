class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            skip = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                res = max(skip, buy)
            if not buying:
                sell = dfs(i + 2, not buying) + prices[i]
                res = max(skip, sell)
            
            memo[(i, buying)] = res
            return res
        
        return dfs(0, True)