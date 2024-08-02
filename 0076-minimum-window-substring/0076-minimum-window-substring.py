class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = defaultdict(int)
        hash_map1 = defaultdict(int)
        
        def helper():
            for k, v in hash_map.items():
                if k not in hash_map1:
                    return False
                
                if hash_map1[k] < v:
                    return False
            return True
        
        for i in t:
            hash_map[i] += 1
        
        res = ""
        min_len = float('inf')
        
        left = right = 0
        
        while right < len(s):
            
            if s[right] in hash_map:
                hash_map1[s[right]] += 1
            
            while helper() and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left : right + 1]
                    
                if s[left] in hash_map:
                    hash_map1[s[left]] -= 1
                    if hash_map1[s[left]] == 0:
                        del hash_map1[s[left]]
                
                left += 1
            
            right += 1
            
        return res
                
                
                
                    
        