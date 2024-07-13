class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            hash_set.add(num)
            
        res = 0
        
        for num in nums:
            if num - 1 not in hash_set:
                temp_res = 0
                while num in hash_set:
                    num += 1
                    temp_res += 1
                
                res = max(res, temp_res)
                
        return res