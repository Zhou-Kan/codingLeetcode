class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        
        for i, j in enumerate(graph):
            for k in j:
                g[i].append(k)
                
        n = len(graph)
        visited = set()
        
        def dfs(i, path):
            #nonlocal n
            if i == n - 1:
                path.append(i)
                res.append(path.copy())
                path.pop()
                return 
            
            if i in visited:
                return 
            
            visited.add(i)
            path.append(i)
            
            for j in g[i]:
                
                dfs(j, path)
                
            visited.remove(i)
            path.pop()
            
        res = []
        dfs(0, [])
        return res
        