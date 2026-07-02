class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minb = prices[0]

        for sell in prices:
            res = max(res, sell - minb)
            minb = min(minb, sell)
        return res