class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bucket = defaultdict(int)
        
        for num in nums:
            bucket[num] += 1
        
        for i in range(10 ** 4, -10 ** 4, -1):
            if i in bucket:
                if k <= bucket[i]:
                    return i
                k -= bucket[i]
            
            
                
        return 0
            
        