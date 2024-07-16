class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        
        left = right = 0
        
        sum_num = 0
        
        while right < len(arr):
            
            sum_num += arr[right]
            
            if right - left + 1 == k:
                
                if sum_num >= threshold * k:
                    res += 1
                    
                sum_num -= arr[left]
                left += 1
                
            right += 1
            
        return res
                
        