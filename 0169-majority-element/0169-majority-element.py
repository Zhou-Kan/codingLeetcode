class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
            if count[num] * 2 > len(nums):
                return num
        