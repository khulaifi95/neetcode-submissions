class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(nums):
            if len(nums) == 2:
                return 0
            
            maxCoin = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(nums[:i] + nums[i + 1:])
                maxCoin = max(maxCoin, coins)
            return maxCoin
        
        return dfs(nums)