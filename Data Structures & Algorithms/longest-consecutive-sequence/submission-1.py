class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snum = set(nums)
        res = 0

        for num in snum:
            if num - 1 not in snum:
                length = 1
                while num + length in snum:
                    length += 1
                res = max(length, res)
        
        return res