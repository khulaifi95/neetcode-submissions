class Solution:

    def dfs(self, src, adj, visited, path, res):
        if src in visited:
            return True
        if src in path:
            return False
        path.add(src)

        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visited, path, res):
                return False
        
        path.remove(src)
        visited.add(src)
        res.append(src)

        return True

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adj list
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
        
        # global
        topSort = []
        visited = set()
        path = set()

        for i in range(n):
            if not self.dfs(i, adj, visited, path, topSort):
                return []
    
        topSort.reverse()
        return topSort