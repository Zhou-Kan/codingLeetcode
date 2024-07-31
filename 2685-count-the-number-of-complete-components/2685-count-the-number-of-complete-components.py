class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
            
        visited = set()
        
        def dfs(i):
            nonlocal e, v
            if i in visited:
                return 
            
            visited.add(i)
            e += 1
            v += len(g[i])
            for j in g[i]:
                dfs(j)
                
        
        res = 0
        
        for i in range(n):
            if i not in visited:
                e = v = 0
                dfs(i)
                if v == e * (e - 1):
                    res += 1
                    
        return res
                