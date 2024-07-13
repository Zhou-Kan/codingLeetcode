class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        n = len(s)
        
        for i in range(2 * n - 1):
            
            l = i // 2
            r = (i + 1) // 2
            
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res
        