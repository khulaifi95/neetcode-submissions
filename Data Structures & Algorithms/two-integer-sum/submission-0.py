class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2idx = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in val2idx:
                return [val2idx[diff], i]
            val2idx[n] = i