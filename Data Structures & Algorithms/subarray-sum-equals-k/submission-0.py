class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        curr_sum = 0

        sum_cnt = { 0: 1 }

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            res += sum_cnt.get(diff, 0)

            sum_cnt[curr_sum] = 1 + sum_cnt.get(curr_sum, 0)
        
        return res