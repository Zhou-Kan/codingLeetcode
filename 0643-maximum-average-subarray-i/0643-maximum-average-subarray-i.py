class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = 0
        
        sum_num = 0
        
        res = float('-inf')
        
        while right < len(nums):
            
            sum_num += nums[right]
            
            if right - left + 1 == k:
                
                res = max(res, sum_num / k)
                
                sum_num -= nums[left]
                
                left += 1
                
            right += 1
        
        
        return res
            
            
            
        