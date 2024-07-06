class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        
        n = len(grid[0])
        
        
        res = 0
        
        def dfs(i, j):
            grid[i][j] = '0'
            
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == '1':
                    dfs(i, j)
                    
                    res += 1
                    
        return res
                            
        