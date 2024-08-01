class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        cur = 0
        
        while cur <= right:
            if nums[cur] == 2 and left <= right:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            
            elif nums[cur] == 0 and left <= right:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1
            
            else:
                cur += 1
        
                
            
            