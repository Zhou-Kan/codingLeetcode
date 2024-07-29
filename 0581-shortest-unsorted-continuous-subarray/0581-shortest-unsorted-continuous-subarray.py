class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = sorted(nums)
        
        left = -1
        
        for i in range(len(nums)):
            if nums[i] != nums_copy[i]:
                left = i
                break
        
        right = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != nums_copy[i]:
                right = i
                break
                
        return right - left + 1 if left != -1 else 0
        