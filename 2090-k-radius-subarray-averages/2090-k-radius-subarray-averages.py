class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        left = 0
        right = 2 * k
        
        if right > n:
            return res
        sum_num = 0
        
        for i in range(right):
            sum_num += nums[i]
        
        while right < n:
            sum_num += nums[right]
            
            res[(left + right) // 2] = sum_num // (2 * k + 1)
            
            right += 1
            
            sum_num -= nums[left]
            left += 1
            
        return res
            
                
                
        
        