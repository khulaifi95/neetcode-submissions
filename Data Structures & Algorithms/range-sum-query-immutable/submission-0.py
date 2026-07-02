class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.prefix = []

        for i in range(len(nums)):
            total += nums[i]
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        sumr = self.prefix[right]
        suml = self.prefix[left - 1] if left > 0 else 0
        return sumr - suml


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)