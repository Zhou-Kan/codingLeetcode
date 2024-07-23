class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = defaultdict(list)
        
        for e, v in edges:
            path[e].append(v)
            path[v].append(e)
            
            
        visited = set()
        
        res = False
        
        def dfs(i):
            nonlocal res
            
            if i == destination:
                res = True
                
            if i in visited:
                return 
            
                
            visited.add(i)
            
            for j in path[i]:
                if j not in visited:
                    dfs(j)
                
        dfs(source)
        
        return res