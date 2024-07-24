class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        res = []
        
        buckets = defaultdict(int)
        
        for i in range(k - 1):
            buckets[nums[i]] += 1
        
        
        left = 0
        right = k - 1
        
        while right < len(nums):
            
            buckets[nums[right]] += 1
            
            count = 0
            
            for i in range(-50, 51):
                if i in buckets:
                    if count == x - 1:
                        res.append(i)
                        break
                    count += buckets[i]
                    if count > x - 1:
                        res.append(i)
                        break

                    

                    
            if res and res[-1] > 0:
                res[-1] = 0
                
            buckets[nums[left]] -= 1
            if buckets[nums[left]] == 0:
                del buckets[nums[left]]
            left += 1            
            right += 1
                
        return res
            
            
            
            
        
        
        