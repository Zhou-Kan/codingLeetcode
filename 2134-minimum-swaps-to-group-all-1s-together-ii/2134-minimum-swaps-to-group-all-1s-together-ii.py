class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        
        total_k = sum(nums[ 0 : total])
        
        res = total - total_k
        
        n = len(nums)
        
        for i in range(1, n):
            total_k += nums[(total + i - 1) % n] - nums[i - 1]
            
            res = min(res, total - total_k)
            
            
        return res
        
        
        