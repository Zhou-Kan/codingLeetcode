class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cur_max = nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            res = max(res, cur_max)
        
        return res
        