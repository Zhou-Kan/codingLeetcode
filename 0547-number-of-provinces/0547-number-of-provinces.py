class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        g = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    g[i].append(j)
                    g[j].append(i)
                        
        visited = set()
        
        res = 0
        
        def dfs(i):
            if i in visited:
                return 
            
            visited.add(i)
            
            for j in g[i]:
                if j not in visited:
                    #visited.add(j)
                    dfs(j)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
                
        return res
                    
                
        