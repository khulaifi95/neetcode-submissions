
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        curr = 0 
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            elif x > y:
                # negative > is <
                curr = y - x
                heapq.heappush(stones, curr)
            else:
                curr = x - y
                heapq.heappush(stones, curr)
        return -stones[0] if len(stones) > 0 else 0
