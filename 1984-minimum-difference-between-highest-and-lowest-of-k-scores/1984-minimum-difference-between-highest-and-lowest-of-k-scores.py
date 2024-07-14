class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        
        left = right = 0
        
        res = float('inf')
        
        while right < len(nums):
            
            if right - left + 1 == k:
                res = min(res, nums[right] - nums[left])
                left += 1
                
            right += 1
        return res