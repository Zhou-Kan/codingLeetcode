class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        
        for e, v in edges:
            g[v].append(e)
            
        def dfs(i):
            if visited[i]:
                return
            
            visited[i] = True
            
            for j in g[i]:
                dfs(j)
                
        ans = [[] for _ in range(n)]
        
        for i in range(n):
            visited = [False] * n 
            dfs(i)
            visited[i] = False
            for j in range(n):
                if visited[j]:
                    ans[i].append(j)
                    
        return ans
            
            
        