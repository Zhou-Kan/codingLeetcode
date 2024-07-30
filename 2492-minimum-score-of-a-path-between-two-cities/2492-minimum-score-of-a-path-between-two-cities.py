class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for i, j, k in roads:
            g[i].append((j, k))
            g[j].append((i, k))
            
        res = float('inf')
        
        visited = set()
        def dfs(i):
            nonlocal res
            if i in visited:
                return 
            
            visited.add(i)
            
            for j in g[i]:
                res = min(res, j[1])
                dfs(j[0])
            
        dfs(1)
        return res
            