class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        single_sum = 0
        double_sum = 0
        
        for num in nums:
            if num >= 0 and num < 10:
                single_sum += num
                
            if num >= 10 and num <= 99:
                double_sum += num
                
        if single_sum > total_sum - single_sum or double_sum > total_sum - double_sum:
            return True
        
        return False
        