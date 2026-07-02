class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        res = [0 for _ in range(len(temperatures))]
        stk = []
        for i, temp in enumerate(temperatures):
            # while temp is warmer than the temp at the index on top of stack
            while stk and temp > temperatures[stk[-1]]:
                # we get the previous index and we know it has a larger temp
                prev_idx = stk.pop()
                res[prev_idx] = i - prev_idx
            stk.append(i)
        return res