class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = defaultdict(list)
        
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            
        n = len(nums)
        
        for i, j in freq.items():
            buckets[j].append(i)
            
        
        res = []
        for i in range(n, -1, -1):
            if i in buckets:
                res += buckets[i]
            if k == len(res):
                break
                
        return res
        