class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1 or sum(nums) == 0 or len(nums) == sum(nums):
            return 0
        counts = sum(nums)
        
        
        length = len(nums) - counts
        
        res = float('inf')
        
        num_sum = 0
        
        for i in range(length - 1):
            num_sum += nums[i]
            
        left = 0
        right = length - 1
        
        while right < len(nums):
            num_sum += nums[right]
            
            res = min(res, num_sum)
            
            num_sum -= nums[left]
            left += 1
            right += 1
            
        num_sum = 0
        for i in range(counts - 1):
            num_sum += nums[i]
            
        left = 0
        right = counts - 1
        
        while right < len(nums):
            num_sum += nums[right]
            
            res = min(res, counts - num_sum)
            
            num_sum -= nums[left]
            left += 1
            right += 1
            
        return res