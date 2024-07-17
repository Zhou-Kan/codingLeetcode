class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left = 0
        right = k - 1
        
        res = float('inf')
        operations = 0
        
        for i in range(k - 1):
            if blocks[i] == 'W':
                operations += 1
                
                
        while right < len(blocks):
                if blocks[right] == 'W':
                    operations += 1
                    
                res = min(res, operations)
                
                
                if blocks[left] == 'W':
                    operations -= 1
                
                left += 1
                right += 1
                
                
        return res if res != float('inf') else operations
        
        
        