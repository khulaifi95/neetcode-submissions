class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        minh = [(0, k)]
        visited = set()
        t = 0

        while minh:
            w1, n1 = heapq.heappop(minh)
            if n1 in visited:
                continue
            visited.add(n1)
            t = w1

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minh, (w1 + w2, n2))
        return t if len(visited) == n else -1