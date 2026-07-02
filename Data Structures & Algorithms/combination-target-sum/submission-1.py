class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def backtrack(i):
            if i >= len(nums):
                return
            if sum(curr) >= target:
                if sum(curr) == target:
                    res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i)
            curr.pop()
            backtrack(i + 1)
        
        backtrack(0)

        return res