class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i, num in enumerate(nums[:-1]):
            if num > nums[i + 1]:
                return nums[i + 1]
        return nums[0]