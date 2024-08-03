class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hash_map = defaultdict(int)
        
        for i, v in enumerate(nums):
            if target - v in hash_map:
                return [i, hash_map[target - v]]
            
            hash_map[v] = i
        