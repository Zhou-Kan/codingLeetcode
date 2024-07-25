class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hash_map1 = defaultdict(int)
        hash_map2 = defaultdict(int)
        
        for s in s1:
            hash_map1[s] += 1
            
        for i in range(len(s1) - 1):
            hash_map2[s2[i]] += 1
            
        left = 0 
        right = len(s1) - 1
        while right < len(s2):
            hash_map2[s2[right]] += 1
            
            if hash_map1 == hash_map2:
                return True
            
            hash_map2[s2[left]] -= 1
            if hash_map2[s2[left]] == 0:
                del hash_map2[s2[left]]
            
            left += 1
            right += 1
        
        return False
        