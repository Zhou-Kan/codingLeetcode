class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = float('-inf')
        
        sum_nums = 0
        
        hash_map = defaultdict(int)
        

        for i in range(k - 1):
            hash_map[nums[i]] += 1
            sum_nums += nums[i]
            
        left = 0 
        right = k - 1
        
        while right < len(nums):
            sum_nums += nums[right]
            hash_map[nums[right]] += 1
            
            if len(hash_map) >= m:
                res = max(res, sum_nums)
                
            sum_nums -= nums[left]
            hash_map[nums[left]] -= 1
            if hash_map[nums[left]] == 0:
                del hash_map[nums[left]]
                
            left += 1
            right += 1
            
        return res if res != float('-inf') else 0