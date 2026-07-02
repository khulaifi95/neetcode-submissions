class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prev_idx = stk.pop()
                res[prev_idx] = i - prev_idx
            stk.append(i)
        return res