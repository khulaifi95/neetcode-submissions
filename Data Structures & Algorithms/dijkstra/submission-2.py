class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for s, d, w in edges:
            adj[s].append((d, w))

        shortest = {}
        minh = [(0, src)]

        while minh:
            cost, vertex = heapq.heappop(minh)
            if vertex in shortest:
                continue
            shortest[vertex] = cost

            for each_d, each_w in adj[vertex]:
                if each_d not in shortest:
                    heapq.heappush(minh, (each_w + cost, each_d))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest