class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        count = defaultdict(int)
        
        res = [0] * (len(nums) - k + 1)
        
        for num in nums[:k - 1]:
            count[num] += 1
            
        for i, (right, left) in enumerate(zip(nums[k - 1:], nums)):
            count[right] += 1
            
            total = x
            
            for j in range(-50, 0):
                total -= count[j]
                if total <= 0:
                    
                    res[i] = j
                    break
            
            count[left] -= 1
            
        return res
 
            
        