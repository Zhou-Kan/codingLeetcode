class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        in_cur = 0
        out_cur = 0
        
        n = len(customers)
        
        res = 0
        
        for i in range(n):
            if grumpy[i] == 0:
                
                in_cur += customers[i]
                
                
        for i in range(minutes):
            if grumpy[i] == 1:
                
                out_cur += customers[i]
                
                
        left = 0
        right = minutes
        
        res = in_cur + out_cur
        
        while right < len(customers):
            
            if grumpy[right] == 1:
                out_cur += customers[right]
            
            if grumpy[left] == 1:
                out_cur -= customers[left]
                
            res = max(res, in_cur + out_cur)
            left += 1
            right += 1
            
        return res
            
            
                
            
                
                
        
        