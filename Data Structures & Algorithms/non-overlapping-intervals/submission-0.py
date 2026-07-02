"""
intervals = [
    [1, 2],
    [2, 4],
    [1, 4],
]

find: min # of intervals to remove, making non-overlapping

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        def dfs(i, prev):
            if i >= len(intervals):
                return 0
            res = dfs(i + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res
        
        return len(intervals) - dfs(0, -1)
