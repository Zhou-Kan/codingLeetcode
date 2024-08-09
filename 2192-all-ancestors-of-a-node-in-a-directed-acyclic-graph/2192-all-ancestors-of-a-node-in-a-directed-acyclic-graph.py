class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        
        for e, v in edges:
            g[v].append(e)
            
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            
            for j in g[i]:
                dfs(j)
                
        ans = [[] for _ in range(n)]
        
        for i in range(n):
            visited = set()
            dfs(i)
            for j in range(n):
                if j in visited and j != i:
                    ans[i].append(j)
                    
        return ans
            
            
        