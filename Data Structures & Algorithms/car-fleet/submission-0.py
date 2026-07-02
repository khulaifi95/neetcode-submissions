"""
position, speed, len n, target

[1, 4], [3, 2], 10

x1 = 1 + 3t
x2 = 4 + 2t

for each x1, x2:
    if (x2 - x1) // (v2 - v1) <= (target - x2) // v2:
        x1 merge to x2


"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        # first process the farest
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            # multiple times, and recent one got faster
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
