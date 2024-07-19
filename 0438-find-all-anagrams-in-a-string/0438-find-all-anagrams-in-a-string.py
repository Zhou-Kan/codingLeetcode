class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        
        if m > n:
            return res
        
        hash_map = defaultdict(int)
        hash_map1 = defaultdict(int)
        
        for c in p:
            hash_map[c] += 1
            
        
        left = 0
        right = m - 1
        for i in range(m - 1):
            hash_map1[s[i]] += 1
            
        while right < n:
            hash_map1[s[right]] += 1
            
            if hash_map == hash_map1:
                res.append(left)
                
            hash_map1[s[left]] -= 1
            if hash_map1[s[left]] == 0:
                del hash_map1[s[left]]
                
            left += 1
            right += 1
            
        return res
            
            
            
            
            
            
        