class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        
        z = x ^ y
        
        while z:
            res += z & 1
            z >>= 1
            
        return res
        
        