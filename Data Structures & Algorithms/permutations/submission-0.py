class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        used = [False] * len(nums)

        def dfs(nums, track, used):
            if len(track) == len(nums):
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                dfs(nums, track, used)
                track.pop()
                used[i] = False
        dfs(nums, track, used)
        return res