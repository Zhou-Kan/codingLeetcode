class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        g = defaultdict(list)
        
        for e, v in connections:
            g[e].append(v)
            g[v].append(e)
            
        visited = set()
        
        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            
            for j in g[i]:
                dfs(j)
        
        groups = 0
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                groups += 1
        
        return groups - 1