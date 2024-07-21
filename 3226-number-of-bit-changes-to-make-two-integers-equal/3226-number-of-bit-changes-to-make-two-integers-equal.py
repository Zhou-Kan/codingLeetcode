class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n:
            return -1
        
        b1 = bin(n)[2 : ]
        b2 = bin(k)[2 : ]
        
        diff = len(b1) - len(b2)
        
        b2 = '0' * diff + b2 
        
        res = 0
        
        for i in range(len(b1)):
            if b1[i] == '1' and b2[i] == '0':
                res += 1
            
            if b1[i] == '0' and b2[i] == '1':
                return -1
            
        return res