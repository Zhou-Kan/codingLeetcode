class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        
        res = nums[0]
        
        for i in range(1, len(nums)):
            res ^= nums[i]
            
        return res
        