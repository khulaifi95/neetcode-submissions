class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(i):
            res = []
            if i >= len(nums):
                return [[]]
            
            perms = backtrack(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    if pcopy not in res:
                        res.append(pcopy)
            return res
        
        return backtrack(0)