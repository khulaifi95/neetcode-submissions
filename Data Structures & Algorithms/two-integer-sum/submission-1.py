class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2idx = {}
        for idx, num in enumerate(nums):
            if target - num in val2idx:
                return [val2idx[target - num], idx]
            else:
                val2idx[num] = idx