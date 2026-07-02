'''
travel in `days`
tickets:
- 1-day, 7-day, 30-day -> `costs` @ 0, 1, 2

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]

[1, 2, 3, 4, 5, 6, 7, 8]

'''


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def travel(k, td):
            "go to the next stop day."
            for j in range(k + 1, len(days)):
                if days[j] - days[k] < td:
                    continue
                else:
                    return j
            return len(days)
        memo = [-1] * len(days)
        def dfs(i):
            if i >= len(days):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = min(
                costs[0] + dfs(travel(i, 1)),
                costs[1] + dfs(travel(i, 7)),
                costs[2] + dfs(travel(i, 30))
            )
            return memo[i]
                
        return dfs(0)