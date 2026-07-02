"""
position[i] = [1, 4]
speed[i] = [ 3, 2 ]
target = 10


"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet = sorted(list(zip(position, speed)), key=lambda x: x[0])

        # keep track of the expected time to reach target
        stack = deque()

        for i in range(len(fleet) - 1, -1, -1):
            ttt = (target - fleet[i][0]) / fleet[i][1]
            stack.append(ttt)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)